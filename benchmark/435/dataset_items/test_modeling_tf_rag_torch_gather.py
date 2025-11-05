import unittest
import tensorflow as tf

from modeling_tf_rag import torch_gather

class TestTorchGather(unittest.TestCase):

    def setUp(self):
        # Create a sample tensor for testing
        self.param = tf.constant([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=tf.float32)
        self.id_tensor = tf.constant([
            [0],
            [2],
            [1]
        ], dtype=tf.int32)

    def test_torch_gather(self):
        # Expected output
        expected_output = tf.constant([
            [1],
            [6],
            [8]
        ], dtype=tf.float32)
        
        result = torch_gather(self.param, self.id_tensor)
        tf.debugging.assert_equal(result, expected_output)

    def test_dtype_consistency(self):
        # Ensure dtype consistency in indexing
        self.id_tensor = tf.constant([
            [0],
            [2],
            [1]
        ], dtype=tf.int64)  # Change dtype to int64 (the default is int32)

        # Expected output should still be correct
        expected_output = tf.constant([
            [1],
            [6],
            [8]
        ], dtype=tf.float32)

        result = torch_gather(self.param, self.id_tensor)
        tf.debugging.assert_equal(result, expected_output)
    
    def test_more_than_3d_array(self):
        # Create a sample 3D tensor for testing
        self.param = tf.constant([
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
        ], dtype=tf.float32)
        self.id_tensor = tf.constant([
            [[0], [1], [2]],
            [[2], [1], [0]],
            [[1], [0], [2]]
        ], dtype=tf.int32)

        # Expected output
        expected_output = tf.constant([
            [[1], [5], [9]],
            [[12], [14], [16]],
            [[20], [22], [27]]
        ], dtype=tf.float32)
        result = torch_gather(self.param, self.id_tensor)
        print(result)
        tf.debugging.assert_equal(result, expected_output)

if __name__ == '__main__':
    unittest.main()

