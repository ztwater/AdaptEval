import unittest
import os
from urllib.parse import urlparse, unquote
from urllib.request import url2pathname
from multilspy_utils import PathUtils
import ast
import re
import inspect
import importlib
import textwrap
from unittest.mock import patch

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

class TestUriToPath(unittest.TestCase):
    def setUp(self):
        source = textwrap.dedent(inspect.getsource(PathUtils.uri_to_path))
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_windows_path(self):
        uri = "file:///C:/Program Files/Steam/"
        expected = "/C:/Program Files/Steam"
        self.assertEqual(PathUtils.uri_to_path(uri), expected)

    def test_linux_path(self):
        uri = "file:///etc/hosts"
        expected = "/etc/hosts"
        self.assertEqual(PathUtils.uri_to_path(uri), expected)

    def test_absolute_path(self):
        uri = "file:///proc/cpuinfo"
        self.assertEqual(PathUtils.uri_to_path(uri), '/proc/cpuinfo')

    def test_escaped_chars(self):
        uri = "file:///home/user/some%20file.txt"
        expected = "/home/user/some file.txt"
        self.assertEqual(PathUtils.uri_to_path(uri), expected)

    def test_no_authority(self):
        uri = "file:c:/path/to/file"
        expected = "/c:/path/to/file"
        self.assertEqual(PathUtils.uri_to_path(uri), expected)

    def test_no_netloc(self):
        uri = "file:///path/to/file"
        self.assertEqual(PathUtils.uri_to_path(uri), "/path/to/file")

    def test_add_type_annotations(self):
        annotations = PathUtils.uri_to_path.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('uri', annotations)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], str)
        self.assertEqual(annotations['uri'], str)

    def test_urlparse_module_import(self):
        matched_new = re.search(r'from\s+urllib\.parse\s+import\s+urlparse,\s*unquote', self.source)
        self.assertIsNotNone(matched_new)

    def test_url2pathname_module_import(self):
        matched_new = re.search(r'from\s+urllib\.request\s+import\s+url2pathname', self.source)
        self.assertIsNotNone(matched_new)

    def test_encapsulate(self):
        self.assertTrue(hasattr(PathUtils, 'uri_to_path'))
        self.assertTrue(callable(PathUtils.uri_to_path))


if __name__ == '__main__':
    unittest.main()