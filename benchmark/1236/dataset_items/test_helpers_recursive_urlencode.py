import re, ast, inspect
import unittest
from unittest.mock import patch
from typing import Dict
from urllib.parse import quote
from helpers import recursive_urlencode

class TestRecursiveUrlencode(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(recursive_urlencode)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_provided_case(self):
        data = {'a': 'b&c', 'd': {'e': {'f&g': 'h*i'}}, 'j': 'k'}
        expected = 'a=b%26c&d[e][f%26g]=h%2Ai&j=k'
        result = recursive_urlencode(data)
        self.assertEqual(result, expected)

    def test_type_annotations(self):
        annotations = recursive_urlencode.__annotations__
        self.assertEqual(annotations['d'], Dict)

    def test_string_formatting(self):
        matched_format = re.search(r'[\'\"].+[\'\"]\s*%\s*\(.+\)', self.source, re.DOTALL)
        matched_fstring = re.search(r'f[\'\"].*\{.+}.*[\'\"]', self.source, re.DOTALL)
        self.assertIsNone(matched_format)
        self.assertIsNotNone(matched_fstring)

    @patch('urllib.parse.quote', return_value='')
    def test_replace_api(self, mock_quote):
        data = {'a': 'b&c', 'd': {'e': {'f&g': 'h*i'}}, 'j': 'k'}
        recursive_urlencode(data)
        mock_quote.assert_called()

    def test_replace_api_str(self):
        matched_quote = re.search(r'\burllib\.quote\(', self.source)
        self.assertIsNone(matched_quote)

    def test_function_refactoring(self):
        matched_old = re.search(r'def\s+recursion\(', self.source)
        matched_new = re.search(r'def\s+_recursion\(', self.source)
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

if __name__ == "__main__":
    unittest.main()

