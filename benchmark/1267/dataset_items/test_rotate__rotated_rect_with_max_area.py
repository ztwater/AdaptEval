import os
import inspect
import re
import ast
import unittest
from unittest.mock import patch
import math

from rotate import _rotated_rect_with_max_area


class TestRotatedRectWithMaxArea(unittest.TestCase):
    def setUp(self):
        src_path = os.path.join(os.path.dirname(__file__), 'rotate.py')
        with open(src_path, 'r', encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = extract_method_code(source, tree, '_rotated_rect_with_max_area')

    def test_rotate_30(self):
        result = _rotated_rect_with_max_area(10, 5, 30)
        self.assertEqual(result['x_min'], 1)
        self.assertEqual(result['x_max'], 3)
        self.assertEqual(result['y_min'], 2)
        self.assertEqual(result['y_max'], 7)

    def test_rotate_45(self):
        result = _rotated_rect_with_max_area(8, 4, 45)
        self.assertEqual(result['x_min'], 0)
        self.assertEqual(result['x_max'], 3)
        self.assertEqual(result['y_min'], 2)
        self.assertEqual(result['y_max'], 5)

    def test_rotate_60(self):
        result = _rotated_rect_with_max_area(12, 6, 60)
        self.assertEqual(result['x_min'], 0)
        self.assertEqual(result['x_max'], 6)
        self.assertEqual(result['y_min'], 4)
        self.assertEqual(result['y_max'], 7)
    
    def test_rotate_90(self):
        result = _rotated_rect_with_max_area(15, 7, 90)
        self.assertEqual(result['x_min'], 0)
        self.assertEqual(result['x_max'], 7)
        self.assertEqual(result['y_min'], 4)
        self.assertEqual(result['y_max'], 11)

    def test_rotate_120(self):
        result = _rotated_rect_with_max_area(10, 5, 120)
        self.assertEqual(result['x_min'], 0)
        self.assertEqual(result['x_max'], 5)
        self.assertEqual(result['y_min'], 3)
        self.assertEqual(result['y_max'], 6)

    def test_rename_function(self):
        from rotate import _rotated_rect_with_max_area
        self.assertTrue(callable(_rotated_rect_with_max_area))

    def test_swap_parameters(self):
        parameters = inspect.signature(_rotated_rect_with_max_area).parameters
        self.assertEqual(list(parameters)[0], 'h')
        self.assertEqual(list(parameters)[1], 'w')

    def test_delete_if_statement(self):
        result = _rotated_rect_with_max_area(-1, -1, 180)
        self.assertNotEqual(result, (0, 0))

    @patch('math.radians')
    def test_add_angle_conversion(self, mock_radians):
        _rotated_rect_with_max_area(15, 7, 90)
        mock_radians.assert_called_with(90)

    def test_update_return_format(self):
        result = _rotated_rect_with_max_area(10, 5, 30)
        self.assertEqual(len(result), 4)
        self.assertIsInstance(result, dict)
        self.assertIn('x_min', result)
        self.assertIn('x_max', result)
        self.assertIn('y_min', result)
        self.assertIn('y_max', result)

    def test_adjust_floating_point_value(self):
        matched_old = re.search(r'\s2\.\D', self.source)
        matched_new = re.search(r'\s2\.0', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

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

def extract_method_code(file_content, tree, method_name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            start_line = node.lineno - 1  # Lines in ast are 1-indexed
            end_line = node.end_lineno  # End line (only available in Python 3.8+)
            method_lines = file_content.splitlines()[start_line:end_line]
            method_code = '\n'.join(method_lines)
            return method_code


if __name__ == '__main__':
    unittest.main()
