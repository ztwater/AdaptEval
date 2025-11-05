import unittest
from unittest.mock import patch
from typing import Dict
from nested_dict import append_nested_dict
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

class TestAppendNestedDict(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(append_nested_dict)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_rename_function(self):
        import nested_dict
        self.assertTrue(callable(append_nested_dict))
        self.assertNotIn('merge_dict', nested_dict.__dict__)
        self.assertIn('append_nested_dict', nested_dict.__dict__)

    def test_add_type_annotations(self):
        self.assertEqual(append_nested_dict.__annotations__, {'dict1': Dict, 'dict2': Dict, 'return': None})

    def test_remove_return_statement(self):
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        result = append_nested_dict(dict1, dict2)
        self.assertIsNone(result)

    def test_use_isinstance_for_type_check(self):
        matched_old = re.search(r'type\(\s*val\s*\)\s*==\s*dict', self.source)
        matched_new = re.search(r'isinstance\(\s*val\s*,\s*dict\s*\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_use_isinstance_for_comparison(self):
        matched_old = re.search(r'type\(\s*dict2\[key]\s*\)\s*==\s*dict', self.source)
        matched_new = re.search(r'isinstance\(\s*dict2\[key]\s*,\s*dict\s*\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_replace_not_in_check(self):
        matched_old = re.search(r'not\s+key\s+in', self.source)
        matched_new = re.search(r'key\s+not\s+in', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_function(self):
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        append_nested_dict(dict1, dict2)
        expected = {'a': 1, 'b': 2}
        self.assertEqual(dict1, expected)

if __name__ == '__main__':
    unittest.main()
