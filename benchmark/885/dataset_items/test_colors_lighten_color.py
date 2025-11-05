import unittest
from colors import lighten_color
from unittest.mock import patch
from unittest import mock
import inspect
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


class TestLightenColor(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(lighten_color)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_lighten_matplotlib_color(self):
        # Test with a matplotlib color string
        original_color = 'green'
        lightened_color = lighten_color(original_color, 0.3)
        expected_color = (0.5505882352941176, 1, 0.5505882352941176) 
        self.assertEqual(lightened_color, expected_color)

    def test_lighten_hex_color(self):
        # Test with a hex color string
        original_color = '#FF5733'
        lightened_color = lighten_color(original_color, 0.4)
        expected_color = (0.9999999999999999, 0.7364705882352942, 0.68)  # Example expected RGB, should be calculated based on actual result
        self.assertEqual(lightened_color, expected_color)

    def test_lighten_rgb_tuple(self):
        # Test with an RGB tuple
        original_color = (0.5, 0.5, 0.5)  # A grey color
        lightened_color = lighten_color(original_color, 0.5)
        expected_color = (0.75, 0.75, 0.75)  
        self.assertEqual(lightened_color, expected_color)

    def test_lighten_invalid_color(self):
        # Test with an invalid color input
        with self.assertRaises(Exception):
            lighten_color('not_a_color', 0.5)

    def test_lighten_invalid_keyerror(self):
        with self.assertRaises(ValueError) as result:
            lighten_color('non_existent_color', 0.5)

    def test_lighten_invalid_typeerror(self):
        with self.assertRaises(TypeError) as result:
            lighten_color('#F034A3', '0.5')

    def test_import_remove(self):
        matched_import_matplotlib = re.search(r'(import\s+matplotlib)|'
                                              r'(from\s+matplotlib(\.colors)?\s+import)',
                                              self.source)
        matched_import_colorsys = re.search(r'import\s+colorsys', self.source)
        self.assertIsNone(matched_import_matplotlib)
        self.assertIsNone(matched_import_colorsys)





if __name__ == '__main__':
    unittest.main()