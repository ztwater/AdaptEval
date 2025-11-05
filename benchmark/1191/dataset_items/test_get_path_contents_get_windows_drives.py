import unittest
from unittest.mock import patch, MagicMock
from get_path_contents import get_windows_drives
from typing import List
import ast
import re 
import inspect
import string

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

class TestGetWindowsDrives(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(get_windows_drives)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    @patch('ctypes.windll.kernel32.GetLogicalDrives', return_value=0b101)
    @patch('ctypes.windll', create=True)
    @patch('platform.system', return_value='Windows')
    def test_drives_returned(self, mock_platform, mock_windll, mock_get_logical_drives):
        self.assertEqual(get_windows_drives(), ['A:\\', 'C:\\'])

    @patch('ctypes.windll.kernel32.GetLogicalDrives', return_value=0)
    @patch('ctypes.windll', create=True)
    @patch('platform.system', return_value='Windows')
    def test_no_drives(self, mock_platform, mock_windll, mock_get_logical_drives):
        self.assertEqual(get_windows_drives(), [])

    @patch('platform.system', return_value='Linux')
    def test_non_windows_system(self, mock_platform):
        self.assertEqual(get_windows_drives(), [])

    @patch('ctypes.windll.kernel32.GetLogicalDrives',  return_value=0b11001)
    @patch('ctypes.windll', create=True)
    @patch('platform.system', return_value='Windows')
    def test_drives_with_spaces(self, mock_platform, mock_windll, mock_get_logical_drives):
        self.assertEqual(get_windows_drives(), ['A:\\', 'D:\\', 'E:\\'])

    @patch('ctypes.windll.kernel32.GetLogicalDrives', return_value=0b110001)
    @patch('ctypes.windll', create=True)
    @patch('platform.system', return_value='Windows')
    def test_drives_in_different_order(self, mock_platform, mock_windll, mock_get_logical_drives):
        self.assertEqual(get_windows_drives(), ['A:\\', 'E:\\', 'F:\\'])

    def test_add_type_annotations(self):
        annotations = get_windows_drives.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], List[str])

    def test_add_import_statement(self):
        matched_new = re.search(r'from\s+ctypes\s+import\s+windll|import\s+ctypes\.windll', self.source)
        self.assertIsNotNone(matched_new)

    def test_add_ascii_uppercase_by_string(self):
        matched_old = re.search(r'string\.uppercase', self.source)
        matched_new = re.search(r'string\.ascii_uppercase', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    @patch('ctypes.windll', create=True)
    @patch('platform.system', return_value='Windows')
    def test_platform_system(self, mock_platform, mock_windll):
        get_windows_drives()
        mock_platform.assert_called()

    @patch('ctypes.windll.kernel32.GetLogicalDrives', return_value=0b101)
    @patch('ctypes.windll', create=True)
    @patch('platform.system', return_value='Windows')
    def test_ascii_uppercase(self, mock_platform, mock_windll, mock_get_logical_drives):
        class AccessTracker:
            def __init__(self, original):
                self.original = original
                self.access_count = 0

            def __getitem__(self, item):
                self.access_count += 1
                return self.original[item]
            
        ascii_uppercase_tracker = AccessTracker(string.ascii_uppercase)
        with patch('string.ascii_uppercase', ascii_uppercase_tracker):
            get_windows_drives()

        self.assertGreater(ascii_uppercase_tracker.access_count, 0)


if __name__ == '__main__':
    unittest.main()