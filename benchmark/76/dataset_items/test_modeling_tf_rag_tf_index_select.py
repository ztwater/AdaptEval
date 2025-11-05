import unittest
from unittest.mock import patch, MagicMock
import tensorflow as tf
import inspect
import re
import ast
import astunparse

from modeling_tf_rag import tf_index_select

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

class TestTfIndexSelect(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(tf_index_select)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = astunparse.unparse(tree)

    def test_import_shape_list(self):
        source = inspect.getsource(tf_index_select)
        matched_shape_list = re.search(r'shape_list\(\w+\)', self.source)
        self.assertIsNotNone(matched_shape_list)

    def test_has_func_in_module(self):
        import transformers
        self.assertTrue('modeling_tf_utils' in transformers.__dict__)
        self.assertIsNotNone(getattr(transformers.__dict__['modeling_tf_utils'],
                                     'shape_list'))

    def test_2d_tensor_positive_dim(self):
        input_2d = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        indices_2d = [0, 2]
        result_2d = tf_index_select(input_2d, 0, indices_2d)
        expected_2d = tf.constant([[1, 2, 3], [7, 8, 9]])
        self.assertTrue(tf.reduce_all(tf.equal(result_2d, expected_2d)).numpy())
    
    def test_2d_tensor_negative_dim(self):
        input_2d = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        indices_2d = [1, 2]
        result_2d = tf_index_select(input_2d, -1, indices_2d)
        expected_2d = tf.constant([[2, 3], [5, 6], [8, 9]])
        self.assertTrue(tf.reduce_all(tf.equal(result_2d, expected_2d)).numpy())

    def test_1d_tensor(self):
        input_1d = tf.constant([1, 2, 3, 4])
        indices_1d = [1, 3]
        result_1d = tf_index_select(input_1d, 0, indices_1d)
        expected_1d = tf.constant([2, 4])
        self.assertTrue(tf.reduce_all(tf.equal(result_1d, expected_1d)).numpy())

    def test_non_contiguous_indices(self):
        input_nc = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        indices_nc = [2, 0]
        result_nc = tf_index_select(input_nc, 0, indices_nc)
        expected_nc = tf.constant([[7, 8, 9], [1, 2, 3]])
        self.assertTrue(tf.reduce_all(tf.equal(result_nc, expected_nc)).numpy())

if __name__ == "__main__":
    unittest.main()
