import unittest
import numpy as np
from scipy.signal import convolve2d
import inspect,ast,re
from unittest.mock import patch

from _tools import estimate_noise

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


class TestEstimateNoise(unittest.TestCase):
    def setUp(self):
        # Set up any prerequisites for each test
        self.test_image = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=float)
        source = inspect.getsource(estimate_noise)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_string_updates(self):
        matched_old = re.search(r'np\.absolute', self.source)
        matched_new = re.search(r'np\.abs', self.source)
        matched_old2 = re.search(r'math\.sqrt', self.source)
        matched_new2 = re.search(r'np\.sqrt', self.source)
        matched_old3 = re.search(r'math\.pi', self.source)
        matched_new3 = re.search(r'np\.pi', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)
        self.assertIsNone(matched_old2)
        self.assertIsNotNone(matched_new2)
        self.assertIsNone(matched_old3)
        self.assertIsNotNone(matched_new3)

    def test_handle_nan(self):
        data = np.array([[1, 2, np.nan], [4, 5, 6], [7, 8, 9]])
        res = estimate_noise(data)
        self.assertFalse(np.isnan(res))

    def test_update_identifier(self):
        signature = inspect.signature(estimate_noise)
        parameters = signature.parameters
        self.assertIn("data", parameters)
        self.assertNotIn("I", parameters)

    def test_update_variable_naming(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        estimated_noise = estimate_noise(data)
        self.assertIsInstance(estimated_noise, float)

    @patch('numpy.abs', wraps=np.abs)
    @patch('numpy.sqrt', wraps=np.sqrt)
    @patch('numpy.pi', new=3)
    def test_update_function_call(self, mock_sqrt, mock_abs):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        res = estimate_noise(data)
        mock_sqrt.assert_called()
        mock_abs.assert_called()
        self.assertAlmostEqual(res, 18.3711, places=2)

    def test_noise_estimation_with_valid_image(self):
        # Test with a valid image to ensure the function returns a float
        result = estimate_noise(self.test_image)
        self.assertIsInstance(result, float)

    def test_noise_estimation_with_nan_values(self):
        # Test with an image containing NaN values to ensure they are handled
        test_image_with_nan = np.copy(self.test_image)
        test_image_with_nan[1, 1] = np.nan
        result = estimate_noise(test_image_with_nan)
        self.assertIsInstance(result, float)

    def test_noise_estimation_with_large_image(self):
        # Test with a larger image to ensure the function scales well
        large_image = np.random.rand(100, 100)
        result = estimate_noise(large_image)
        self.assertIsInstance(result, float)

    def test_noise_estimation_with_zero_image(self):
        # Test with an image full of zeros to ensure it handles this case
        zero_image = np.zeros((3, 3), dtype=float)
        result = estimate_noise(zero_image)
        self.assertEqual(result, 0.0)

    def test_noise_estimation_with_constant_image(self):
        # Test with an image where all values are the same (but not zero) to check behavior
        constant_image = np.full((3, 3), 1.0, dtype=float)
        result = estimate_noise(constant_image)
        self.assertGreater(result, 0.0)

    def test_noise_estimation_with_negative_values(self):
        # Test with an image containing negative values
        negative_image = np.array([[-1, -2, -1], [-2, -4, -2], [-1, -2, -1]], dtype=float)
        result = estimate_noise(negative_image)
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()
