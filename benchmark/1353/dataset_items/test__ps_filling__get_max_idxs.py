import unittest
from unittest.mock import patch
import numpy as np
import inspect
import re
import ast

from _ps_filling import _get_max_idxs


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


class TestGetMaxIdxs(unittest.TestCase):
    def setUp(self):
        self.arr = np.array([
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        source = inspect.getsource(_get_max_idxs)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_func_rename(self):
        import _ps_filling
        self.assertTrue('_get_max_idxs' in _ps_filling.__dict__)
        self.assertFalse('get_max_idxs' in _ps_filling.__dict__)
        self.assertTrue(callable(_get_max_idxs))

    def test_add_local_filename_parameter(self):
        parameters = inspect.signature(_get_max_idxs).parameters
        self.assertNotIn("row_window", parameters)
        self.assertNotIn("col_window", parameters)
        self.assertEqual("row_looks", list(parameters.keys())[1])
        self.assertEqual("col_looks", list(parameters.keys())[2])

    @patch('numpy.lib.stride_tricks.sliding_window_view', return_value=np.array([[[[1]], [[2]], [[3]], [[4]]]]))
    def test_early_return(self, mock_sliding_window_view):
        rows, cols = _get_max_idxs(self.arr, 1, 1)
        mock_sliding_window_view.assert_not_called()

    def test_single_look(self):
        rows, cols = _get_max_idxs(self.arr, 1, 1)
        expected_rows, expected_cols = np.where(self.arr == self.arr)
        self.assertTrue(np.array_equal(rows, expected_rows))
        self.assertTrue(np.array_equal(cols, expected_cols))

    def test_multiple_looks(self):
        rows, cols = _get_max_idxs(self.arr, 2, 2)
        expected_rows = np.array([1, 1, 3, 3])
        expected_cols = np.array([1, 3, 1, 3])
        self.assertTrue(np.array_equal(rows,expected_rows))
        self.assertTrue(np.array_equal(cols,expected_cols))

if __name__ == '__main__':
    unittest.main()
