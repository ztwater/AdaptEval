import re
import ast
import inspect
import unittest
from common import getattrd

class TestGetattrd(unittest.TestCase):
    class Dummy:
        def __init__(self):
            self.a = 'value_a'
            self.b = self.B()

        class B:
            def __init__(self):
                self.c = 'value_c'

    def setUp(self):
        source = inspect.getsource(getattrd)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_existing_attribute(self):
        obj = self.Dummy()
        self.assertEqual(getattrd(obj, 'a'), 'value_a')
        self.assertEqual(getattrd(obj, 'b.c'), 'value_c')

    def test_nonexistent_attribute_with_default(self):
        obj = self.Dummy()
        self.assertEqual(getattrd(obj, 'x', 'default_value'), 'default_value')

    def test_nonexistent_attribute_without_default(self):
        obj = self.Dummy()
        with self.assertRaises(AttributeError):
            getattrd(obj, 'x')

    def test_change_referenced_api_name(self):
        matched_old = re.search(r'[^.]reduce\(', self.source)
        matched_new = re.search(r'functools\.reduce\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_remove_unused_variable(self):
        match_old = re.search(r'except\s+\w+\s*,\s*e', self.source)
        self.assertIsNone(match_old)

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
