import unittest
import unicodedata
from cnames import _rmdiacritics
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


class TestRmdiacritics(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(_rmdiacritics)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_rmdiacritics_basic(self):
        # Test with a character that has a diacritic
        self.assertEqual(_rmdiacritics('á'), 'a')

    def test_rmdiacritics_no_diacritics(self):
        # Test with a character that has no diacritic
        self.assertEqual(_rmdiacritics('b'), 'b')

    def test_rmdiacritics_invalid_name(self):
        # Test with a character that, when diacritic is removed, results in an invalid name
        self.assertEqual(_rmdiacritics('ẚ'), 'a')

    def test_rmdiacritics_non_ascii(self):
        # Test with a non-ASCII character that has a diacritic
        self.assertEqual(_rmdiacritics('ü'), 'u')

    def test_rmdiacritics_special_cases(self):
        # Test with special cases where the diacritic removal might not be straightforward
        self.assertEqual(_rmdiacritics('ℎ'), '\u210e')  # Special case for 'h' with a bar
        self.assertEqual(_rmdiacritics('ℓ'), '\u2113')  # Special case for 'l' with a bar

    def test_rename_function(self):
        from cnames import _rmdiacritics
        self.assertTrue(callable(_rmdiacritics))

    def test_string_updates(self):
        matched_old_0 = re.search(r'ud\.name\(', self.source)
        matched_old_1 = re.search(r'ud\.lookup\(', self.source)
        matched_new_0 = re.search(r'unicodedata\.name\(', self.source)
        matched_new_1 = re.search(r'unicodedata\.lookup\(', self.source)
        self.assertIsNone(matched_old_0)
        self.assertIsNone(matched_old_1)
        self.assertIsNotNone(matched_new_0)
        self.assertIsNotNone(matched_new_1)
    

# This allows the test script to be run from the command line
if __name__ == '__main__':
    unittest.main()