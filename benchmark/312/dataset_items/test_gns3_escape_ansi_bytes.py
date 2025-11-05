import unittest
import inspect
import ast
import re
from gns3 import escape_ansi_bytes


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

class TestEscapeAnsiBytes(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(escape_ansi_bytes)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_encapsulate_code_in_function(self):
        # Test the encapsulation of code within the function
        input_bytes = b'\x1b[01;31mTest\x1b[00m'
        escape_ansi_bytes(input_bytes)

    def test_add_type_annotations(self):
        annotations = escape_ansi_bytes.__annotations__
        self.assertIn('input', annotations)
        self.assertEqual(annotations['input'], bytes)

    def test_add_return_statement(self):
        # Test the return statement logic
        input_bytes = b'\x1b[01;31mTest\x1b[00m'
        expected_output = b'Test'
        self.assertEqual(escape_ansi_bytes(input_bytes), expected_output)

    def test_rename_variable_ansi_escape(self):
        matched_old = re.search(r'\bansi_escape\b', self.source)
        matched_new = re.search(r'\bansi_escape_8bit\b', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_rename_variable_sometext(self):
        matched_old = re.search(r'\bsometext\b', self.source)
        matched_new = re.search(r'\binput\b', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    # def test_change_regex_pattern_type(self):
    #     input_bytes = b'\x1b[01;31mTest\x1b[00m'
    #     expected_output = b'Test'
    #     with self.assertRaises(TypeError):
    #         escape_ansi_bytes(input_bytes)

    def test_update_regex_pattern(self):
        input_bytes = b'\x1b@\x1b[01;31m\x80Test\x9b;31m'
        expected_output = b'Test'
        self.assertEqual(escape_ansi_bytes(input_bytes), expected_output)

if __name__ == '__main__':
    unittest.main()