import unittest
import numpy as np
import inspect
from parse_rosetta_data import is_outlier
import ast
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

class TestIsOutlier(unittest.TestCase):
    def setUp(self):
        # Initialize the data for testing
        source = inspect.getsource(is_outlier)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)
        self.data_with_outliers = np.array([0, 1, 2, 100, 3, 4, 5])
        self.data_without_outliers = np.array([1, 2, 3, 4, 5, 6])
        self.data_with_zero_mdev = np.array([5])  # All elements are the same

    def test_with_outliers(self):
        # Test data with outliers
        outliers = is_outlier(self.data_with_outliers, m=6.5)
        expected = np.array([False, False, False, True, False, False, False])
        np.testing.assert_array_equal(outliers, expected)

    def test_without_outliers(self):
        # Test data without outliers
        outliers = is_outlier(self.data_without_outliers, m=6.5)
        expected = np.array([False, False, False, False, False, False])
        np.testing.assert_array_equal(outliers, expected)

    def test_with_zero_mdev(self):
        # Test data where the median absolute deviation is zero
        outliers = is_outlier(self.data_with_zero_mdev, m=6.5)
        expected = np.array([False])  # No comparison is made, all are considered as not outliers
        np.testing.assert_array_equal(outliers, expected)

    def test_default_m_value(self):
        # Test the default m value
        outliers = is_outlier(self.data_with_outliers)
        expected = np.array([False, False, False, True, False, False, False])
        np.testing.assert_array_equal(outliers, expected)

    def test_function_rename(self):
        import parse_rosetta_data
        self.assertNotIn('reject_outliers', parse_rosetta_data.__dict__)
        self.assertTrue(callable(is_outlier))

    def test_add_type_annotations(self):
        parameters = inspect.signature(is_outlier).parameters
        self.assertEqual(parameters['m'].default, 6.5)

    def test_update_return_value(self):
        outliers = is_outlier(self.data_with_outliers, m=6.5)
        self.assertIsInstance(outliers[0], np.bool_)

    def test_simplify_division(self):
        matched_old = re.search(r'else\s+np\.zeros\(\s*len\(\s*d\s*\)\s*\)', self.source)
        matched_new = re.search(r'else\s+0(\.)?', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)


if __name__ == '__main__':
    unittest.main()
