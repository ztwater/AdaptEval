import unittest
import numpy as np
import math
from unittest.mock import patch
import inspect
import ast
import re

from misc import fibonacci_sphere


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


class TestFibonacciSphere(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(fibonacci_sphere)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_function_returns_n_points(self):
        """Tests if the function returns the specified number of points."""
        num_points = 100
        points = fibonacci_sphere(num_points)
        self.assertEqual(len(points), num_points)

    def test_return_numpy_array(self):
        num_points = 10
        points = fibonacci_sphere(num_points)
        self.assertEqual(type(points), np.ndarray)
        self.assertNotEqual(type(points), list)

    def test_points_on_unit_sphere(self):
        """Tests if all points lie on a unit sphere."""
        num_points = 100
        points = fibonacci_sphere(num_points)
        distances = np.linalg.norm(points, axis=1)
        self.assertTrue(np.allclose(distances, 1.0))

    def test_point_representation_list(self):
        matched_tuple = re.search(r'append\(\(x,\s*y,\s*z\)\)', self.source)
        matched_list = re.search(r'append\(\[x,\s*y,\s*z]\)', self.source)
        self.assertIsNone(matched_tuple)
        self.assertIsNotNone(matched_list)

    def test_numpy_function_usage(self):
        matched_math = re.search(r'math\.', self.source)
        matched_numpy = re.search(r'np\.|numpy\.', self.source)
        self.assertIsNone(matched_math)
        self.assertIsNotNone(matched_numpy)

    def test_rename_method_parameter(self):
        signature = inspect.signature(fibonacci_sphere)
        # Check if the method has the correct annotations
        parameters = signature.parameters
        self.assertEqual("N", list(parameters.keys())[0])
        self.assertEqual("N", str(parameters['N']))


if __name__ == "__main__":
    unittest.main()