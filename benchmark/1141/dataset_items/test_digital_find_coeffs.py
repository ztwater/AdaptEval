import unittest
import numpy as np
import ast
import re
from unittest.mock import patch
import inspect

# Assuming the find_coeffs function is in a module named perspective_transform
from digital import find_coeffs

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

class TestFindCoeffs(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(find_coeffs)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_correct_input_output(self):
        pa = [(1, 2), (2, 2), (2, 1), (1, 1)]
        pb = [(10, 20), (20, 20), (20, 10), (10, 10)]
        expected = np.array([10, 0, 0, 0, 10, 0, 0, 0])  # Example expected result
        result = find_coeffs(pa, pb)
        np.testing.assert_array_almost_equal(result, expected)

    def test_invalid_point_format(self):
        with self.assertRaises(ValueError):
            find_coeffs([(1, 2), (3, 'x'), (5, 6), (7, 8)], [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_equal_points(self):
        pa = [(1, 1), (1, 1), (1, 1), (1, 1)]
        pb = [(2, 2), (2, 2), (2, 2), (2, 2)]
        with self.assertRaises(ValueError):  # Assuming this raises an error
            find_coeffs(pa, pb)

    def test_non_square_input(self):
        with self.assertRaises(ValueError):
            find_coeffs([(1, 2), (3, 4)], [(5, 6), (7, 8)])  # Only two points

    def test_numerical_stability(self):
        # Create a matrix that is close to singular
        pa = [(1, 1), (1 + 1e-9, 1), (1, 1 + 1e-9), (1 + 1e-9, 1 + 1e-9)]
        pb = [(2, 2), (2, 2), (2, 2), (2, 2)]
        with self.assertRaises(np.linalg.LinAlgError):  # Assuming this raises a LinAlgError
            find_coeffs(pa, pb)

    def test_update_alias(self):
        matched_old = re.search(r'\bnumpy\.(matrix|array|float|linalg)', self.source)
        matched_new = re.search(r'\bnp.(matrix|array|float|linalg)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)


    def test_update_dtype(self):
        pa = [(1, 2), (2, 2), (2, 1), (1, 1)]
        pb = [(10, 20), (20, 20), (20, 10), (10, 10)]
        return_value = np.matrix([[1, 2, 1, 0, 0, 0, -10, -20],
                                       [0, 0, 0, 1, 2, 1, -20, -40],
                                       [2, 2, 1, 0, 0, 0, -40, -40],
                                       [0, 0, 0, 2, 2, 1, -40, -40],
                                       [2, 1, 1, 0, 0, 0, -40, -20],
                                       [0, 0, 0, 2, 1, 1, -20, -10],
                                       [1, 1, 1, 0, 0, 0, -10, -10],
                                       [0, 0, 0, 1, 1, 1, -10, -10]], dtype=np.float64)

        with patch("numpy.matrix", return_value=return_value) as mock_matrix:
            find_coeffs(pa, pb)
            self.assertEqual(mock_matrix.call_args.kwargs['dtype'], np.float64)
    

if __name__ == '__main__':
    unittest.main()