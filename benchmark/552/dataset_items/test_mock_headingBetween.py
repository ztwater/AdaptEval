import os.path
import unittest
import math
import re
import inspect
import ast
import numpy as np
from unittest.mock import patch

from mock import MockCamera


class TestHeadingBetween(unittest.TestCase):
    def setUp(self):
        self.camera = MockCamera()
        src_path = os.path.join(os.path.dirname(__file__), 'mock.py')
        with open(src_path, 'r', encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = extract_method_code(source, tree, 'headingBetween')

    def test_heading_between_same_points(self):
        self.assertEqual(self.camera.headingBetween(0, 0, 0, 0), 0)

    def test_heading_between_opposite_points(self):
        self.assertEqual(self.camera.headingBetween(0, 0, 0, 180), 90)

    def test_heading_between_north_south(self):
        self.assertEqual(self.camera.headingBetween(0, 0, 90, 0), 0)
        self.assertEqual(self.camera.headingBetween(90, 0, 0, 0), 180)

    def test_heading_between_east_west(self):
        self.assertEqual(self.camera.headingBetween(0, 0, 0, 90), 270)
        self.assertEqual(self.camera.headingBetween(0, 0, 0, -90), 90)

    def test_heading_between_crossing_prime_meridian(self):
        self.assertEqual(self.camera.headingBetween(0, -10, 0, 10), 270)

    def test_heading_between_crossing_equator(self):
        self.assertEqual(self.camera.headingBetween(10, 0, -10, 0), 180)

    def test_heading_between_negative_longitude(self):
        self.assertEqual(self.camera.headingBetween(0, -10, 0, 10), 270)

    def test_heading_between_negative_latitude(self):
        self.assertEqual(self.camera.headingBetween(-10, 0, 10, 0), 0)

    def test_change_function_name_and_type(self):
        self.camera.headingBetween(0, 0, 0, 0)

    def test_remove_semicolon(self):
        matched_semicolon = re.search(r';\s*\n', self.source)
        self.assertIsNone(matched_semicolon)

    @patch('math.degrees', return_value=90)
    @patch('numpy.rad2deg', return_value=90)
    def test_change_api_call(self, mock_np, mock_math):
        self.camera.headingBetween(0, 0, 0, 0)
        mock_np.assert_not_called()
        mock_math.assert_called()

    def test_rename_var(self):
        matched_old = re.search(r'\bbrng\b', self.source)
        matched_new = re.search(r'\bbearing\b', self.source)
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
