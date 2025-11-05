import unittest
from unittest.mock import patch, MagicMock
import inspect

from get_latest_checkpoint import download_as_bytes_with_progress
 
EXAMPLE_SRC = "https://meadow-canid-fb5.notion.site/AdaptEval-Annotation-Guideline-aae4cc72b1c04d63b8a169ed1b4e8cea"# "https://arxiv.org/pdf/1712.04609"# 'http://example.com'


class TestDownloadAsBytesWithProgress(unittest.TestCase):
    @patch('requests.get')
    def test_functional_correctness(self, mock_get):
        mock_response = MagicMock()
        mock_response.headers = {'content-length': '100'}
        mock_response.iter_content = lambda chunk_size: [b'0' * chunk_size] * 2
        mock_get.return_value = mock_response

        result = download_as_bytes_with_progress(EXAMPLE_SRC)
        self.assertEqual(result, b'0' * 65536 * 2)

    def test_optional_name_parameter_added(self):
        signature = inspect.signature(download_as_bytes_with_progress)
        self.assertIn("name", signature.parameters)
        param = signature.parameters["name"]
        self.assertEqual(param.annotation, str)
        self.assertEqual(param.default, None)

    @patch('tqdm.tqdm')
    @patch('requests.get')
    def test_optional_name_parameter_work(self, mock_get, mock_tqdm):
        mock_response = MagicMock()
        mock_response.headers = {'content-length': '100'}
        mock_response.iter_content = lambda chunk_size: [b'0' * chunk_size] * 2
        mock_get.return_value = mock_response
        download_as_bytes_with_progress(EXAMPLE_SRC, name='Test Download')
        self.assertEqual(mock_tqdm.call_args.kwargs['desc'], 'Test Download')

    @patch('requests.get')
    def test_allow_redirects(self, mock_get):
        mock_response = MagicMock()
        mock_response.headers = {'content-length': '100'}
        mock_response.iter_content = lambda chunk_size: [b'0' * chunk_size] * 2
        mock_get.return_value = mock_response

        download_as_bytes_with_progress(EXAMPLE_SRC)
        mock_get.assert_called_with(EXAMPLE_SRC, stream=True, allow_redirects=True)

    @patch('tqdm.tqdm')
    @patch('requests.get')
    def test_default_name(self, mock_get, mock_tqdm):
        mock_response = MagicMock()
        mock_response.headers = {'content-length': '100'}
        mock_response.iter_content = lambda chunk_size: [b'0' * chunk_size] * 2
        mock_get.return_value = mock_response
        download_as_bytes_with_progress(EXAMPLE_SRC)
        self.assertEqual(mock_tqdm.call_args.kwargs['desc'], EXAMPLE_SRC)

if __name__ == "__main__":
    unittest.main()
