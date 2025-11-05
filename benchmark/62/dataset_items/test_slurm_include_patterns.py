import os
import unittest
import inspect
import re
import ast

from slurm import include_patterns


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


class TestIncludePatterns(unittest.TestCase):


    def setUp(self):
        # Setup a sample directory structure in memory (mocking)
        self.src_directory = 'src'
        self.dst_directory = 'dst'
        self.files = ['file1.txt', 'file2.dwg', 'file3.dxf', 'dir1']

        # Mock os.path.isdir
        self.original_isdir = os.path.isdir
        os.path.isdir = lambda path: path.endswith('dir1')

        # Mock os.path.join
        self.original_join = os.path.join
        os.path.join = lambda a, b: f"{a}/{b}"

        source = inspect.getsource(include_patterns)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def tearDown(self):
        # Restore the original functions
        os.path.isdir = self.original_isdir
        os.path.join = self.original_join

    def test_include_patterns_filter(self):
        # Test to ensure fnmatch.filter is used correctly
        ignore_function = include_patterns('*.dwg', '*.dxf')
        ignored_files = ignore_function(self.src_directory, self.files)
        self.assertNotIn('file2.dwg', ignored_files)
        self.assertNotIn('file3.dxf', ignored_files)

    def test_include_patterns_isdir(self):
        # Test to ensure os.path.isdir is used correctly
        ignore_function = include_patterns('*.dwg', '*.dxf')
        ignored_files = ignore_function(self.src_directory, self.files)
        self.assertIn('file1.txt', ignored_files)
        self.assertNotIn('dir1', ignored_files)

    def test_include_patterns_join(self):
        # Test to ensure os.path.join is used correctly
        ignore_function = include_patterns('*.dwg', '*.dxf')
        ignored_files = ignore_function(self.src_directory, self.files)
        expected_ignore = {'file1.txt'}
        self.assertEqual(ignored_files, expected_ignore)

    def test_replace_filter(self):
        matched_old = re.search(r'[^.]filter\(', self.source)
        matched_new = re.search(r'\bfnmatch\.filter\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_replace_path(self):
        matched_isdir_old = re.search(r'[^.]isdir\(', self.source)
        matched_join_old = re.search(r'[^.]join\(', self.source)
        matched_isdir_new = re.search(r'\bos\.path\.isdir\(', self.source)
        matched_join_new = re.search(r'\bos\.path\.join\(', self.source)
        self.assertIsNone(matched_isdir_old)
        self.assertIsNone(matched_join_old)
        self.assertIsNotNone(matched_isdir_new)
        self.assertIsNotNone(matched_join_new)

if __name__ == '__main__':
    unittest.main()

