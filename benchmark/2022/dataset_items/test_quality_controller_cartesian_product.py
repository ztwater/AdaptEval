import unittest
import numpy as np
from quality_controller import cartesian_product
import ast
import inspect
import re

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

class TestCartesianProduct(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(cartesian_product)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_cartesian_product_two_arrays(self):
        x = np.array([1, 2, 3])
        y = np.array([4, 5])
        expected = np.array([[1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]])
        result = cartesian_product(x, y)
        np.testing.assert_array_equal(result, expected)

    def test_cartesian_product_three_arrays(self):
        x = np.array([1, 2])
        y = np.array([3, 4, 5])
        z = np.array([6])
        expected = np.array([[1, 3, 6], [1, 4, 6], [1, 5, 6],
                             [2, 3, 6], [2, 4, 6], [2, 5, 6]])
        result = cartesian_product(x, y, z)
        np.testing.assert_array_equal(result, expected)

    def test_cartesian_product_different_dtypes(self):
        x = np.array([1, 2], dtype=np.int32)
        y = np.array([3.5, 4.5], dtype=np.float64)
        expected_dtype = np.result_type(np.int32, np.float64)
        result = cartesian_product(x, y)
        self.assertEqual(result.dtype, expected_dtype)

    def test_cartesian_product_empty_arrays(self):
        x = np.array([])
        y = np.array([1, 2, 3])
        expected = np.empty((0, 2))
        result = cartesian_product(x, y)
        np.testing.assert_array_equal(result, expected)
        self.assertEqual(result.shape, expected.shape)

    def test_cartesian_product_single_element_arrays(self):
        x = np.array([1])
        y = np.array([2])
        expected = np.array([[1, 2]])
        result = cartesian_product(x, y)
        np.testing.assert_array_equal(result, expected)

    def test_cartesian_product_large_arrays(self):
        x = np.arange(1000)
        y = np.ones(1000)
        result = cartesian_product(x, y)
        self.assertEqual(result.shape, (1000000, 2))

    def test_numpy_result_type_import(self):
        matched_old = re.search(r'numpy\.result_type', self.source)
        matched_new = re.search(r'np\.result_type', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_numpy_empty_import(self):
        matched_old = re.search(r'numpy\.empty', self.source)
        matched_new = re.search(r'np\.empty', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_numpy_ix__import(self):
        matched_old = re.search(r'numpy\.ix_', self.source)
        matched_new = re.search(r'np\.ix_', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)


if __name__ == '__main__':
    unittest.main()