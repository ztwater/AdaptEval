from download_pretrained_model import download_file
import unittest
from unittest.mock import patch, MagicMock, mock_open
import requests
import inspect


class TestDownloadFile(unittest.TestCase):
    def test_add_local_filename_parameter(self):
        signature = inspect.signature(download_file)
        # Check if the method has the correct annotations
        parameters = signature.parameters
        self.assertEqual("local_filename", list(parameters.keys())[1])

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_download_file_default_chunk_size(self, mock_open, mock_get):
        mock_response = MagicMock()
        mock_response.iter_content = MagicMock(return_value=[b'test data'])
        mock_response.__enter__.return_value = mock_response
        mock_get.return_value = mock_response

        result = download_file('http://example.com/file', 'file.txt')

        mock_get.assert_called_once_with('http://example.com/file', stream=True)
        mock_response.raise_for_status.assert_called_once()
        mock_open.assert_called_once_with('file.txt', 'wb')
        handle = mock_open()
        handle.write.assert_called_once_with(b'test data')
        self.assertEqual(result, 'file.txt')

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_update_api_argument(self, mock_open, mock_get):
        mock_response = MagicMock()
        mock_response.iter_content = MagicMock(return_value=[b'test data'])
        mock_response.__enter__.return_value = mock_response
        mock_get.return_value = mock_response
        result = download_file('http://example.com/file', 'file.txt')
        mock_response.iter_content.assert_called_once_with(chunk_size=None)

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_download_file_no_chunk(self, mock_open, mock_get):
        mock_response = MagicMock()
        mock_response.iter_content = MagicMock(return_value=[b''])
        mock_response.__enter__.return_value = mock_response
        mock_get.return_value = mock_response

        result = download_file('http://example.com/file', 'file.txt')

        mock_get.assert_called_once_with('http://example.com/file', stream=True)
        mock_response.raise_for_status.assert_called_once()
        mock_open.assert_called_once_with('file.txt', 'wb')
        handle = mock_open()
        handle.write.assert_called_once_with(b'')
        self.assertEqual(result, 'file.txt')

if __name__ == '__main__':
    unittest.main()