import unittest
import tensorflow as tf
import numpy as np
import inspect
from unittest.mock import patch, call, MagicMock, Mock
import importlib
import ast
import re
import astunparse

from tf_util import batch_norm_template


class CommentRemover(ast.NodeVisitor):
    def visit_Expr(self, node):
        if isinstance(node.value, ast.Str):
            # Preserve docstrings and regular strings
            self.generic_visit(node)
        elif isinstance(node.value, ast.Constant):
            # Skip over comments (which are stored as Constant nodes)
            pass
        else:
            self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Skip over function decorators
        node.decorator_list = []
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Skip over async function decorators
        node.decorator_list = []
        self.generic_visit(node)


class TestBatchNormTemplate(unittest.TestCase):

    def setUp(self):
        tf.reset_default_graph()
        self.inputs = tf.constant(np.random.randn(100, 20, 20, 3), dtype=tf.float32)
        self.is_training = tf.placeholder(tf.bool, shape=())
        self.scope = "bn"
        self.moments_dims = [0, 1, 2]
        self.bn_decay = 0.9

        source = inspect.getsource(batch_norm_template)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = astunparse.unparse(tree)

    def test_training_phase_statistics(self):
        bn_output = batch_norm_template(self.inputs, self.is_training, self.scope, self.moments_dims, self.bn_decay)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            result = sess.run(bn_output, feed_dict={self.is_training: True})
            result_mean = np.mean(result, axis=(0, 1, 2))
            result_var = np.var(result, axis=(0, 1, 2))

            # Check if the means are close to 0
            self.assertTrue(np.allclose(result_mean, np.zeros_like(result_mean), atol=1e-1))

            # Check if the variances are close to 1
            self.assertTrue(np.allclose(result_var, np.ones_like(result_var), atol=1e-1))

    def test_inference_phase_stability(self):
        bn_output = batch_norm_template(self.inputs, self.is_training, self.scope, self.moments_dims, self.bn_decay)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            # Simulate training phase to update moving averages
            for _ in range(50):
                sess.run(bn_output, feed_dict={self.is_training: True})
            # Test inference stability
            inference_result1 = sess.run(bn_output, feed_dict={self.is_training: False})
            inference_result2 = sess.run(bn_output, feed_dict={self.is_training: False})

            # Check if outputs are stable across multiple inference runs
            self.assertTrue(np.allclose(inference_result1, inference_result2, atol=1e-6))

    def test_parameter_renaming(self):
        signature = inspect.signature(batch_norm_template)
        parameters = signature.parameters
        self.assertEqual("inputs", list(parameters.keys())[0])
        self.assertEqual("is_training", list(parameters.keys())[1])
        self.assertEqual("scope", list(parameters.keys())[2])
        self.assertEqual("moments_dims", list(parameters.keys())[3])
        self.assertEqual("bn_decay", list(parameters.keys())[4])

    def test_num_channels(self):
        num_channels = self.inputs.get_shape()[-1].value
        const1 = tf.constant(0.0, shape=[num_channels])
        const2 = tf.constant(1.0, shape=[num_channels])

        with patch('tensorflow.constant', side_effect=[const1, const2]) as mock_tf_constant:
            bn_output = batch_norm_template(self.inputs, self.is_training, self.scope, self.moments_dims, self.bn_decay)
            expected_list = [call(0.0, shape=[num_channels]), call(1.0, shape=[num_channels])]
            self.assertEqual(mock_tf_constant.call_args_list, expected_list)

    def test_decay_value(self):
        ema = tf.train.ExponentialMovingAverage(decay=0.9)
        with patch('tensorflow.train.ExponentialMovingAverage') as mock_train_ema:
            mock_train_ema.return_value = ema
            bn_output = batch_norm_template(self.inputs, self.is_training, self.scope, self.moments_dims, None)
            bn_output = batch_norm_template(self.inputs, self.is_training, self.scope, self.moments_dims, 0.8)
            mock_train_ema.assert_has_calls([call(decay=0.9), call(decay=0.8)])

    def test_assign_scope(self):
        matched_assign = re.search(r'with\s*tf\.variable_scope\(scope\)\s*as\s*sc:\s*', self.source)
        self.assertIsNotNone(matched_assign)

    def test_modify_batch_mean_and_var_calculation(self):
        inputs = tf.constant(np.random.randn(100, 20, 20, 2), dtype=tf.float32)
        moments_dims = [0, 1]
        bm, bv = tf.nn.moments(inputs, moments_dims, name='moments')
        with patch('tensorflow.nn.moments') as mock_nn_moments:
            mock_nn_moments.return_value = (bm, bv)
            bn_output = batch_norm_template(inputs, self.is_training, self.scope, moments_dims, self.bn_decay)
            mock_nn_moments.assert_has_calls([call(inputs, moments_dims, name='moments')])

    def test_update_ema_op(self):
        with patch('tensorflow.no_op', side_effect=tf.no_op) as mock_no_op:
            bn_output = batch_norm_template(self.inputs, tf.constant(False, dtype=tf.bool), self.scope, self.moments_dims, self.bn_decay)

            with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                # Simulate training phase to update moving averages
                for _ in range(50):
                    sess.run(bn_output, feed_dict={self.is_training: True})
                # Test inference stability
                inference_result1 = sess.run(bn_output, feed_dict={self.is_training: False})
                inference_result2 = sess.run(bn_output, feed_dict={self.is_training: False})
                # Check if outputs are stable across multiple inference runs
                # self.assertTrue(np.allclose(inference_result1, inference_result2, atol=1e-6))

            mock_no_op.assert_called()



if __name__ == '__main__':
    unittest.main()

