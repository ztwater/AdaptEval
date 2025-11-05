import unittest
from unittest.mock import patch
from helper import murmur3
import inspect, ast, re
import os

def extract_method_code(file_content, tree, method_name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            start_line = node.lineno - 1  # Lines in ast are 1-indexed
            end_line = node.end_lineno  # End line (only available in Python 3.8+)
            method_lines = file_content.splitlines()[start_line:end_line]
            method_code = '\n'.join(method_lines)
            return method_code


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

class TestMurmur3(unittest.TestCase):
    """
    The expected murmur hashes is calculated with [Online MurmurHash](https://murmurhash.shorelabs.com/)
    """
    def setUp(self):
        src_path = os.path.join(os.path.dirname(__file__), 'helper.py')
        with open(src_path, 'r', encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = extract_method_code(source, tree, 'murmur3')

    def test_func_rename(self):
        import helper
        self.assertTrue(callable(murmur3))
        self.assertTrue('murmur3' in helper.__dict__)
        self.assertFalse('murmur3_x86_32' in helper.__dict__)

    @patch('builtins.ord')
    def test_remove_ord(self, mock_ord):
        murmur3(b"hello, world!")
        mock_ord.assert_not_called()

    def test_refactor_hex(self):
        matched_old = re.search(r'\b0x(?=\w*[a-z])[a-z0-9]+', self.source)
        matched_new = re.search(r'\b0x[A-Z0-9]+', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_empty_string(self):
        self.assertEqual(murmur3(b""), 0)

    def test_single_byte_string(self):
        self.assertEqual(murmur3(b"a"), 1009084850)

    def test_multi_byte_string(self):
        self.assertEqual(murmur3(b"hello, world!"), 3967868818)

    def test_with_seed(self):
        self.assertEqual(murmur3(b"data", seed=1), 582321661)

    def test_different_input_strings(self):
        self.assertNotEqual(murmur3(b"string1"), murmur3(b"string2"))

    def test_func_name_change(self):
        self.assertNotEqual(murmur3.__name__,"murmur3_x86_32")

    def test_different_seed(self):
        data = b"hello"
        seed = 42
        self.assertNotEqual(murmur3(data, seed), murmur3(data))

if __name__ == "__main__":
    unittest.main()
