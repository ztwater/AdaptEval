import unittest
import os
import re
import ast
import inspect
from unittest.mock import patch, mock_open
from io import StringIO

from cgmInitialize import find_files

class TestFindFiles(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_dir'
        os.mkdir(self.test_dir)
        with open(os.path.join(self.test_dir, 'test1.rar'), 'w') as f:
            f.write('some data')
        with open(os.path.join(self.test_dir, 'test2.txt'), 'w') as f:
            f.write('some data')
        with open(os.path.join(self.test_dir, 'test3.rar'), 'w') as f:
            f.write('some data')

        source = inspect.getsource(find_files)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def tearDown(self):
        # Clean up the temporary directory and files after tests
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_find_files_with_rar_pattern(self):
        # Test that the function finds .rar files correctly
        pattern = '*.rar'
        expected = ['test1.rar', 'test3.rar']
        self.assertEqual(set(find_files(self.test_dir, pattern)), set(expected))

    def test_find_files_with_txt_pattern(self):
        pattern = '*.txt'
        expected = ['test2.txt']
        self.assertEqual(find_files(self.test_dir, pattern), expected)

    @patch('builtins.open', new_callable=mock_open, read_data='test data')
    def test_find_files_with_mocked_open(self, mock_file):
        # Test that the function behaves correctly when os.listdir is mocked
        with patch('os.listdir', return_value=['test1.rar', 'test2.txt']):
            with patch('os.path.isfile', return_value=True):
                result = find_files(self.test_dir, '*.rar')
                self.assertEqual(result, ['test1.rar'])

    def test_insert_imports(self):
        matched_os = re.search(r'import\s+os', self.source)
        matched_fnmatch = re.search(f'import\s+fnmatch', self.source)
        self.assertIsNotNone(matched_os)
        self.assertIsNotNone(matched_fnmatch)


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


# This is the entry point for the test script
if __name__ == '__main__':
    unittest.main()