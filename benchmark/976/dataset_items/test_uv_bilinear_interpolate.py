import inspect, re, ast
import unittest
import numpy as np
from unittest.mock import patch, MagicMock, call
from uv import bilinear_interpolate

class TestBilinearInterpolate(unittest.TestCase):
    
    def setUp(self):
        # 设置测试前的准备工作，例如定义测试用例需要的输入和预期输出
        self.img = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
        self.x = 1.5
        self.y = 1.5
        self.expected_result = np.array([7.])

        source = inspect.getsource(bilinear_interpolate)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_functional_correctness(self):
        result = bilinear_interpolate(self.img, self.x, self.y)
        self.assertIsInstance(result, np.ndarray)
        np.testing.assert_array_almost_equal(result, self.expected_result, decimal=5)

    @patch("numpy.asarray", return_value=np.array(1.5))
    def test_remove_asarray_conversions(self, mock_asarray):
        bilinear_interpolate(self.img, self.x, self.y)
        mock_asarray.assert_not_called()

    def test_change_parameter_name(self):
        parameters = inspect.signature(bilinear_interpolate).parameters
        self.assertNotIn('im', parameters)
        self.assertIn('img', parameters)

    def test_update_variable_types(self):
        mock_tmp = MagicMock()
        mock_floor = MagicMock(return_value=mock_tmp)
        np.floor = mock_floor
        bilinear_interpolate(self.img, self.x, self.y)
        mock_floor.assert_has_calls([call(self.x), call(self.y)])
        mock_tmp.astype.assert_called_with(np.int32)

    def test_rename_variables(self):
        matched_old = re.search(r'I[abcd]\s*=', self.source)
        matched_new = re.search(r'i_[abcd]\s*=', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_update_return_statement(self):
        result = bilinear_interpolate(self.img, self.x, self.y)
        self.assertIsInstance(result, np.ndarray)


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


if __name__ == '__main__':
    unittest.main()

