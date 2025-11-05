import re
import inspect
import ast
import unittest
from _memory_viz import _format_size

class TestFormatSize(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(_format_size)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_zero(self):
        # Test with zero to ensure it returns '0B'
        self.assertEqual(_format_size(0), '0.0B')

    def test_bytes(self):
        # Test with values less than 1024 to ensure it returns 'X.YB'
        self.assertEqual(_format_size(999), '999.0B')
        self.assertEqual(_format_size(1023), '1023.0B')

    def test_kilobytes(self):
        # Test with values in the kilobyte range
        self.assertEqual(_format_size(1024), '1.0KiB')
        self.assertEqual(_format_size(2048), '2.0KiB')

    def test_megabytes(self):
        # Test with values in the megabyte range
        self.assertEqual(_format_size(1024**2), '1.0MiB')
        self.assertEqual(_format_size(2*1024**2), '2.0MiB')

    def test_gigabytes(self):
        # Test with values in the gigabyte range
        self.assertEqual(_format_size(1024**3), '1.0GiB')
        self.assertEqual(_format_size(5*1024**3), '5.0GiB')

    def test_terabytes(self):
        # Test with values in the terabyte range
        self.assertEqual(_format_size(1024**4), '1.0TiB')

    def test_petabytes(self):
        # Test with values in the petabyte range
        self.assertEqual(_format_size(1024**5), '1.0PiB')

    def test_exabytes(self):
        # Test with values in the exabyte range
        self.assertEqual(_format_size(1024**6), '1.0EiB')

    def test_zettabytes(self):
        # Test with values in the zettabyte range
        self.assertEqual(_format_size(1024**7), '1.0ZiB')

    def test_yottabytes(self):
        # Test with values in the yottabyte range
        self.assertEqual(_format_size(1024**8), '1.0YiB')

    def test_negative_values(self):
        # Test with negative values to ensure it handles them correctly
        self.assertEqual(_format_size(-1024**3), '-1.0GiB')

    def test_edge_case_1023(self):
        # Test with the edge case of 1023 to ensure it rounds down correctly
        self.assertEqual(_format_size(1023.999), '1024.0B')

    def test_edge_case_1024(self):
        # Test with the edge case of 1024 to ensure it rounds up correctly
        self.assertEqual(_format_size(1024), '1.0KiB')

    def test_adaptation_remove_suffix_parameter(self):
        # Test to ensure the 'suffix' parameter has been removed
        # Expected behavior: the function should not accept a 'suffix' parameter
        with self.assertRaises(TypeError):
            _format_size(1024, suffix="B")

    def test_update_function_name(self):
        from _memory_viz import _format_size

    def test_update_iterable_type(self):
        matched_old = re.search(r'for\s+\w+\s+in\s+\(.*\)', self.source, re.DOTALL)
        matched_new = re.search(r'for\s+\w+\s+in\s+\[.*]', self.source, re.DOTALL)
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


if __name__ == '__main__':
    unittest.main()