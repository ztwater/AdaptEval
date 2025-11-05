import unittest
import inspect
import inspect
import ast
import re
import os

from hacks import inject_hacks

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

def extract_method_code(file_content, tree, method_name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            start_line = node.lineno - 1  # Lines in ast are 1-indexed
            end_line = node.end_lineno  # End line (only available in Python 3.8+)
            method_lines = file_content.splitlines()[start_line:end_line]
            method_code = '\n'.join(method_lines)
            return method_code

class TestNewGetfile(unittest.TestCase):
    def setUp(self):
        src_path = os.path.join(os.path.dirname(__file__), 'hacks.py')
        with open(src_path, 'r', encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = extract_method_code(source, tree, '__new_getfile')

        inject_hacks()

    def test_class_defined_globally(self):
        class TestClass:
            pass
        expected_source = '''        class TestClass:
            pass
'''     
        self.assertEqual(inspect.getsource(TestClass), expected_source)

    def test_getfile_replacement(self):
        source_new_getfile = inspect.getsource(inspect.getfile)
        matched = re.search(r'if\s+not\s*inspect\.isclass\(object\):\n\s+return\s+_old_getfile\(object\)', source_new_getfile)
        self.assertIsNotNone(matched)

    def test_if_condition(self):
        matched_old = re.search(r'if\s+inspect\.isfunction', self.source)
        matched_new = re.search(r'if\s*\(\s*inspect\.isfunction', self.source, re.MULTILINE)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)


if __name__ == '__main__':
    unittest.main()