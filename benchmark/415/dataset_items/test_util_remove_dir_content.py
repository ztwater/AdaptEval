import unittest
import os
import shutil
import tempfile
import inspect
import re
import ast

from util import remove_dir_content


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

class TestRemoveDirContent(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        source = inspect.getsource(remove_dir_content)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_function_parameter(self):
        # Test that the function accepts a directory parameter
        self.assertEqual(remove_dir_content.__code__.co_argcount, 1)
        self.assertIn('directory', remove_dir_content.__code__.co_varnames)

    def test_remove_files(self):
        # Create some test files
        for i in range(5):
            with open(os.path.join(self.test_dir, f'test_file_{i}.txt'), 'w') as f:
                f.write('This is a test file.')

        remove_dir_content(self.test_dir)

        # Check that the directory is empty
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_remove_directories(self):
        # Create some test directories
        for i in range(5):
            os.makedirs(os.path.join(self.test_dir, f'test_dir_{i}'))

        remove_dir_content(self.test_dir)

        # Check that the directory is empty
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_remove_mixed_content(self):
        # Create some test files and directories
        for i in range(5):
            with open(os.path.join(self.test_dir, f'test_file_{i}.txt'), 'w') as f:
                f.write('This is a test file.')
            os.makedirs(os.path.join(self.test_dir, f'test_dir_{i}'))

        remove_dir_content(self.test_dir)

        # Check that the directory is empty
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_handle_exceptions(self):
        # Create a file that should cause an exception
        problematic_file = os.path.join(self.test_dir, 'problematic_file.txt')
        with open(problematic_file, 'w') as f:
            f.write('This is a problematic test file.')

        # Simulate a condition that will cause an exception by mocking os.unlink
        original_unlink = os.unlink

        def mock_unlink(path):
            if path == problematic_file:
                raise Exception("Mocked exception for testing")
            return original_unlink(path)

        os.unlink = mock_unlink

        try:
            remove_dir_content(self.test_dir)
        finally:
            os.unlink = original_unlink

        # Check that the file still exists due to the exception
        self.assertTrue(os.path.exists(problematic_file))

    def test_encapsulate(self):
        from util import remove_dir_content

    def test_remove_hardcoded_directory_path(self):
        matched_str = re.search(r'(folder|[A-Za-z_]\w*)\s*=\s*\'.*\'', self.source)
        self.assertIsNone(matched_str)

if __name__ == '__main__':
    unittest.main()


