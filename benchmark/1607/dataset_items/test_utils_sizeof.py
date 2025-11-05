import unittest
import inspect
import ast
import re

from ctx_utils import sizeof


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

class TestSizeof(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(sizeof)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_zero_size(self):
        # Test file size of 0
        self.assertEqual(sizeof(0), "0.0B")

    def test_single_byte(self):
        # Test file size of 1 byte
        self.assertEqual(sizeof(1), "1.0B")

    def test_kilobyte(self):
        # Test file size just below 1 kilobyte
        self.assertEqual(sizeof(1023), "1023.0B")
        self.assertEqual(sizeof(1024), "1.0KiB")

    def test_megabyte(self):
        # Test file size just below 1 megabyte
        self.assertEqual(sizeof(1024**2 - 1), "1024.0KiB")
        # Test exactly 1 megabyte
        self.assertEqual(sizeof(1024**2), "1.0MiB")

    def test_gigabyte(self):
        # Test file size just below 1 gigabyte
        self.assertEqual(sizeof(1024**3 - 1), "1024.0MiB")
        # Test exactly 1 gigabyte
        self.assertEqual(sizeof(1024**3), "1.0GiB")

    def test_terabyte(self):
        # Test file size just below 1 terabyte
        self.assertEqual(sizeof(1024**4 - 1), "1024.0GiB")
        # Test exactly 1 terabyte
        self.assertEqual(sizeof(1024**4), "1.0TiB")

    def test_negative_size(self):
        # Test file size just below 1 terabyte
        self.assertEqual(sizeof(-1024**4 - 1), "-1.0TiB")
        # Test exactly 1 terabyte
        self.assertEqual(sizeof(-1024**4), "-1.0TiB")

    def test_suffix_customization(self):
        # Test file size with a custom suffix
        self.assertEqual(sizeof(1024, suffix="byte"), "1.0Kibyte")

    def test_rename_function(self):
        import ctx_utils
        self.assertTrue(callable(sizeof))
        self.assertNotIn('sizeof_fmt', ctx_utils.__dict__)

    def test_add_temp_variable(self):
        matched_new = re.search(r'\w+\s*=\s*f?[\'\"].*[\'\"]', self.source)
        self.assertIsNotNone(matched_new)

    def test_f_format_return(self):
        matched_old = re.search(r'return\s+f[\'\"].*[\'\"]', self.source, re.DOTALL)
        matched_new = re.search(r'return\s+\w+\.format\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)
    
if __name__ == '__main__':
    unittest.main()