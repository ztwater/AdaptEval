import unittest
from unittest.mock import patch
import functools
from datetime import datetime, timedelta
import re, ast, inspect

from util import cache

class TestCache(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(cache)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_default_sample(self):
        @cache()
        def test_func(x):
            return x

        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 1, 1, 0, 0, 0)
            self.assertEqual(test_func(1), 1)
            mock_datetime.now.return_value = datetime(2023, 1, 1, 0, 0, 30)
            self.assertEqual(test_func(1), 1)
            mock_datetime.now.return_value = datetime(2023, 1, 1, 0, 1, 1)
            self.assertEqual(test_func(2), 2)

    def test_change_default_ttl(self):
        parameters = inspect.signature(cache).parameters
        self.assertEqual(parameters['ttl'].default, timedelta(minutes=1))

    def test_change_referenced_api_name(self):
        matched_old = re.search(r'\bdatetime\.(datetime|timedelta)', self.source)
        matched_new = re.search(r'[^.](datetime|timedelta)', self.source)
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