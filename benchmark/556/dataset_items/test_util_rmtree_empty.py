import os
import re
import ast
import inspect
import shutil
import unittest
from unittest import TestCase, mock
from tempfile import mkdtemp
from contextlib import contextmanager
from typing import MutableSet

from util import rmtree_empty


@contextmanager
def temporary_directory():
    dir_path = mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)


class TestRmtreeEmpty(TestCase):
    def setUp(self):
        # Set up a temporary directory for each test
        self.test_dir = None
        source = inspect.getsource(rmtree_empty)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_empty_directory_deletion(self):
        with temporary_directory() as dir_path:
            self.test_dir = dir_path
            # create an empty directory
            empty_dir = os.path.join(dir_path, 'empty_dir')
            os.makedirs(empty_dir)
            # create a file for the root directory
            with open(os.path.join(self.test_dir, 'file.txt'), 'w') as f:
                f.write('content')
            # Call the function to delete empty directories
            deleted_dirs = rmtree_empty(dir_path)
            self.assertIn(empty_dir, deleted_dirs)
            self.assertTrue(os.path.exists(dir_path))
            self.assertFalse(os.path.exists(empty_dir))

    def test_non_empty_directory_preservation(self):
        with temporary_directory() as dir_path:
            self.test_dir = dir_path
            # Create a non-empty directory
            non_empty_dir = os.path.join(dir_path, 'non_empty_dir')
            os.makedirs(non_empty_dir)
            with open(os.path.join(non_empty_dir, 'file.txt'), 'w') as f:
                f.write('content')
            deleted_dirs = rmtree_empty(dir_path)
            self.assertNotIn('non_empty_dir', deleted_dirs)
            self.assertTrue(os.path.exists(non_empty_dir))

    def test_nested_empty_directories(self):
        with temporary_directory() as dir_path:
            self.test_dir = dir_path
            with open(os.path.join(self.test_dir, 'file.txt'), 'w') as f:
                f.write('content')
            # Create nested empty directories
            os.makedirs(os.path.join(dir_path, 'a', 'b', 'c'))
            deleted_dirs = rmtree_empty(dir_path)
            # Check that all nested empty directories are deleted
            self.assertIn(os.path.join(dir_path, 'a'), deleted_dirs)
            self.assertIn(os.path.join(dir_path, 'a', 'b'), deleted_dirs)
            self.assertIn(os.path.join(dir_path, 'a', 'b', 'c'), deleted_dirs)
            self.assertFalse(os.path.exists(os.path.join(dir_path, 'a', 'b', 'c')))
            self.assertFalse(os.path.exists(os.path.join(dir_path, 'a', 'b')))
            self.assertFalse(os.path.exists(os.path.join(dir_path, 'a')))

    def test_add_annotations(self):
        annotations = rmtree_empty.__annotations__
        expected = {
            'root': str,
            'return': MutableSet[str]
        }
        self.assertEqual(annotations, expected)

    def test_rename_function(self):
        from util import rmtree_empty

    def test_simplify_file_check(self):
        matched_any_cont = re.search(r'if\s+any\(files\):\s+continue', self.source)
        self.assertIsNotNone(matched_any_cont)

    def test_simplify_subdir_check(self):
        matched_any_sub = re.search(r'if\s+any\(.+\s+not\s+in\s+deleted\s+for.+in\s+subdirs\s*\)', self.source, re.DOTALL)
        self.assertIsNotNone(matched_any_sub)


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