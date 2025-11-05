import inspect
import re
import ast
import unittest
from unittest.mock import patch, mock_open
import requests
from io import BytesIO

from ctx_utils import download_gdrive

class TestDownloadGdrive(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(download_gdrive)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    @patch('ctx_utils.requests.Session')
    def test_download_gdrive_success(self, MockSession):
        mock_session_instance = MockSession.return_value
        mock_response = mock_session_instance.get.return_value
        mock_response.iter_content.return_value = [b'data chunk']
        mock_response.cookies = {'download_warning': 'token'}

        gdrive_id = 'GDRIVE_FILE_ID'
        fname_save = '/path/to/save/file.txt'

        with patch('builtins.open', mock_open()) as mock_file:
            download_gdrive(gdrive_id, fname_save)

        # Assert the two expected calls to session.get()
        mock_session_instance.get.assert_any_call(
            'https://docs.google.com/uc?export=download&confirm=t',
            params={'id': gdrive_id},
            stream=True
        )
        mock_session_instance.get.assert_any_call(
            'https://docs.google.com/uc?export=download&confirm=t',
            params={'id': gdrive_id, 'confirm': 'token'},
            stream=True
        )
        mock_file.return_value.write.assert_called_once_with(b'data chunk')

    @patch('ctx_utils.requests.Session')
    @patch('builtins.print')
    def test_download_gdrive_print_statements(self, mock_print, MockSession):
        mock_session_instance = MockSession.return_value
        mock_response = mock_session_instance.get.return_value
        mock_response.iter_content.return_value = [b'data chunk']
        mock_response.cookies = {'download_warning': 'token'}

        gdrive_id = 'GDRIVE_FILE_ID'
        fname_save = '/path/to/save/file.txt'

        with patch('builtins.open', mock_open()) as mock_file:
            download_gdrive(gdrive_id, fname_save)

        mock_print.assert_any_call('Download started: path={} (gdrive_id={})'.format(fname_save, gdrive_id))
        mock_print.assert_any_call('Download finished: path={} (gdrive_id={})'.format(fname_save, gdrive_id))

    def test_rename_function(self):
        from ctx_utils import download_gdrive
        self.assertTrue(callable(download_gdrive))

    def test_rename_parameters(self):
        parameters = inspect.signature(download_gdrive).parameters
        self.assertNotIn('id', parameters)
        self.assertNotIn('destination', parameters)
        self.assertIn('gdrive_id', parameters)
        self.assertIn('fname_save', parameters)

    def test_rename_base_url_identifier(self):
        matched_old = re.search(r'\bURL\s*=\s*["\']', self.source)
        matched_new = re.search(r'\burl_base\s*=\s*["\']', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_update_base_url(self):
        matched_new = re.search(r'https://.*confirm=t', self.source, re.DOTALL)
        self.assertIsNotNone(matched_new)

    def test_move_functions(self):
        matched_func_0 = re.search(r'def\s+get_confirm_token\(', self.source)
        matched_func_1 = re.search(r'def\s+save_response_content\(', self.source)
        self.assertIsNotNone(matched_func_0)
        self.assertIsNotNone(matched_func_1)


    @patch('ctx_utils.requests.Session')
    def test_session_closing(self, MockSession):
        mock_session_instance = MockSession.return_value
        mock_response = mock_session_instance.get.return_value
        mock_response.iter_content.return_value = [b'data chunk']
        mock_response.cookies = {'download_warning': 'token'}

        gdrive_id = 'GDRIVE_FILE_ID'
        fname_save = '/path/to/save/file.txt'

        with patch('builtins.open', mock_open()) as mock_file:
            download_gdrive(gdrive_id, fname_save)

        mock_session_instance.close.assert_called()

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
