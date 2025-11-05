from _import_from_source import detect_type_checking_mode_modules_names
import unittest
import sys
from unittest.mock import patch
import ast
import inspect
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


class TestDetectTypeCheckingModeModulesNames(unittest.TestCase):
    def setUp(self):
        # Set up any necessary prerequisites before each test
        source = inspect.getsource(detect_type_checking_mode_modules_names)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_detect_type_checking_mode_modules_names(self):
        result = detect_type_checking_mode_modules_names('test')
        expected = {'abc', 'mock'}
        self.assertEqual(set(result), expected)

    def test_import_module_string_updates(self):
        matched_old = re.search(r'importlib\.import_module\(', self.source)
        matched_new = re.search(r'[^.]import_module\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_reload_string_updates(self):
        matched_old = re.search(r'importlib\.reload\(', self.source)
        matched_new = re.search(r'[^.]reload\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)


if __name__ == '__main__':
    unittest.main()