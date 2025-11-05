import re, ast, inspect
import unittest
from unittest.mock import patch
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

from colors import generate_colors

class TestGenerateColors(unittest.TestCase):

    def setUp(self):
        self.nlabels = 10

        source = inspect.getsource(generate_colors)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_function_behavior(self):
        randRGBcolors, colormap = generate_colors(self.nlabels)
        self.assertEqual(len(randRGBcolors), self.nlabels)
        self.assertIsInstance(colormap, LinearSegmentedColormap)
        self.assertNotEqual(colormap(0), (0.0, 0.0, 0.0, 1.0))
        self.assertEqual(colormap(self.nlabels - 1), (0.0, 0.0, 0.0, 1.0))

    def test_rename_method(self):
        from colors import generate_colors
        self.assertTrue(callable(generate_colors))

    def test_change_default_values(self):
        parameters = inspect.signature(generate_colors).parameters
        self.assertEqual(parameters['first_color_black'].default, False)
        self.assertEqual(parameters['last_color_black'].default, True)
        self.assertEqual(parameters['verbose'].default, False)

    @patch('builtins.range')
    def test_xrange_to_range(self, mock_range):
        mock_range.return_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        randRGBcolors, colormap = generate_colors(self.nlabels, type='bright')
        mock_range.assert_called()

    def test_remove_local_imports(self):
        matched_import_map = re.search(r'from\s+matplotlib\.colors\s+import\s+LinearSegmentedColormap', self.source)
        matched_import_colorsys = re.search(r'import\s+colorsys', self.source)
        matched_import_numpy = re.search(r'import\s+numpy', self.source)
        self.assertIsNone(matched_import_map)
        self.assertIsNone(matched_import_colorsys)
        self.assertIsNone(matched_import_numpy)

    def test_update_return_value(self):
        return_values = generate_colors(self.nlabels)
        self.assertEqual(len(return_values), 2)
        self.assertEqual(len(return_values[0]), self.nlabels)
        self.assertIsInstance(return_values[1], LinearSegmentedColormap)

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
