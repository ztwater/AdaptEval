import pathlib
import unittest
from pathlib import Path
import tempfile
import ast
import re
import inspect

from ctx_utils import is_directory_writable

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


class TestIsDirectoryWritable(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(is_directory_writable)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_add_type_annotation(self):
        annotations = is_directory_writable.__annotations__
        self.assertIn('path', annotations)
        self.assertEqual(annotations['path'], pathlib.Path)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], bool)

    def test_rename_error(self):
        matched_e = re.search(r'\be\b', self.source)
        matched_error = re.search(r'\berror\b', self.source)
        self.assertIsNone(matched_e)
        self.assertIsNotNone(matched_error)

    def test_writable_directory(self):
        """Tests if the function correctly identifies a writable directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            self.assertTrue(is_directory_writable(Path(temp_dir)))

    def test_non_writable_directory(self):
        """Tests if the function correctly identifies a non-writable directory."""
        import os
        # Create a temporary directory with restricted permissions
        temp_dir = tempfile.mkdtemp()
        # Windows do not support chmod.
        os.chmod(temp_dir, 0o400)  # Set read-only permissions
        try:
            self.assertFalse(is_directory_writable(Path(temp_dir)))
        finally:
            os.chmod(temp_dir,0o700)  # Restore permissions before deletion
            os.rmdir(temp_dir)

    def test_invalid_path(self):
        """Tests if the function handles invalid paths."""
        self.assertRaises(OSError, is_directory_writable, "?invalid_path")


if __name__ == "__main__":
    unittest.main()
