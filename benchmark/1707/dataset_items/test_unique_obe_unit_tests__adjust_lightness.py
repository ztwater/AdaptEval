import unittest
import matplotlib.colors as mc
import colorsys
from unique_obe_unit_tests import _adjust_lightness
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


class TestAdjustLightness(unittest.TestCase):

    def setUp(self):
        # This method will run before each test function.
        # You can set up any prerequisites for your tests here.
        source = inspect.getsource(_adjust_lightness)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_adjust_lightness_with_matplotlib_color(self):
        # Test the function with a matplotlib color string.
        result = _adjust_lightness('red')
        self.assertEqual(result, (0.5, 0.0, 0.0))  # Expected result should be adjusted lightness of red.

    def test_adjust_lightness_with_hex_color(self):
        # Test the function with a hex color string.
        result = _adjust_lightness('#FF0000')
        self.assertEqual(result, (0.5, 0.0, 0.0))  # Expected result should be adjusted lightness of red.

    def test_adjust_lightness_with_rgb_tuple(self):
        # Test the function with an RGB tuple.
        result = _adjust_lightness((1.0, 0.0, 0.0))
        self.assertEqual(result, (0.5, 0.0, 0.0))  # Expected result should be adjusted lightness of red.

    def test_adjust_lightness_with_amount(self):
        # Test the function with different amounts.
        result = _adjust_lightness('blue', amount=0.2)
        self.assertEqual(result, (0.0, 0.0, 0.2))  # Expected result should be lighter blue.

    def test_adjust_lightness_with_max_lightness(self):
        # Test the function with the maximum lightness.
        result = _adjust_lightness('green', amount=1.0)
        self.assertEqual(result, (0.0, 0.5019607843137255, 0.0))  # Expected result should be the lightest green.

    def test_adjust_lightness_with_min_lightness(self):
        # Test the function with the minimum lightness.
        result = _adjust_lightness('yellow', amount=0.0)
        self.assertEqual(result, (0.0, 0.0, 0.0))  # Expected result should be the darkest yellow.

    def test_adjust_lightness_with_invalid_color(self):
        # Test the function with an invalid color input.
        with self.assertRaises(ValueError):
            _adjust_lightness('not_a_color')

    def test_delete_import(self):
        matched_matplotlib = re.search(r'import\s+matplotlib\.colors\s+as\s+mc', self.source)
        matched_colorsys = re.search(r'import\s+colorsys', self.source)
        self.assertIsNone(matched_matplotlib)
        self.assertIsNone(matched_colorsys)

    def test_rename_function(self):
        import unique_obe_unit_tests
        self.assertTrue(callable(_adjust_lightness))
        self.assertNotIn('adjust_lightness', unique_obe_unit_tests.__dict__)

if __name__ == '__main__':
    unittest.main()