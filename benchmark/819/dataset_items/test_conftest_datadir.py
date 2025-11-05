import unittest
import os
import inspect
from unittest.mock import MagicMock, patch, mock_open
from io import StringIO
import re
import ast
from conftest import datadir
from types import FunctionType


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

class TestDatadir(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(datadir)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    # @patch('distutils.dir_util.copy_tree')
    # @patch('shutil.copytree')
    def test_update_function_call(self):
        matched_old = re.search(r'(dir_util\.)?copy_tree\(', self.source)
        matched_new = re.search(r'(shutil\.)?copytree\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_bytes_string_updates(self):
        matched_old = re.search(r'bytes\(\w+\)', self.source)
        self.assertIsNone(matched_old)
        matched_new = re.search(r'str\(\w+\)', self.source)
        self.assertIsNotNone(matched_new)


    def test_rename_parameter(self):
        parameters = inspect.signature(datadir).parameters
        self.assertIn('tmppath', parameters)

if __name__ == '__main__':
    unittest.main()