import unittest
import tqdm
from unittest.mock import patch, mock_open, MagicMock 
from requests.models import Response 
import inspect

from download import _download_with_progress_bar


class TestDownloadWithProgressBar(unittest.TestCase):
    def setUp(self):
        self.BASE_URL = "https://dl.fbaipublicfiles.com/DGRL/"
        self.ENV_NAMES = [
            "bigfish",
            "bossfight",
            "caveflyer",
            "chaser",
            "climber",
            "coinrun",
            "dodgeball",
            "fruitbot",
            "heist",
            "jumper",
            "leaper",
            "maze",
            "miner",
            "ninja",
            "plunder",
            "starpilot",
        ]

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    @patch('tqdm.std.tqdm.__enter__', wraps=tqdm.tqdm)
    def test_download_with_progress_bar(self, mock_tqdm, mock_open, mock_requests_get):
        url = self.BASE_URL
        file_path = self.ENV_NAMES[0]
        # Mocking the response object
        mock_response = MagicMock(spec=Response)
        mock_response.iter_content = MagicMock(return_value=[b'data1', b'data2', b'data3'])
        mock_response.headers = {'content-length': '15'}
        mock_requests_get.return_value = mock_response
        
        mock_open.return_value.write.return_value = 15
        mock_tqdm.__enter__.return_value = mock_tqdm

        # Call the function
        _download_with_progress_bar(url, file_path)

        # Assertions to ensure the function works correctly
        mock_requests_get.assert_called_once_with(url, stream=True)
        mock_open.assert_called_once_with(file_path, 'wb')
        mock_tqdm.assert_called_once()
        handle = mock_open()
        handle.write.assert_has_calls([unittest.mock.call(b'data1'), unittest.mock.call(b'data2'), unittest.mock.call(b'data3')])

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    @patch('tqdm.std.tqdm.__enter__', wraps=tqdm.tqdm)
    def test_download_with_progress_bar_no_content_length(self, mock_tqdm, mock_open, mock_requests_get):
        url = self.BASE_URL
        file_path = self.ENV_NAMES[0]
        
        # Mocking the response object
        mock_response = MagicMock(spec=Response)
        mock_response.iter_content = MagicMock(return_value=[b'data1', b'data2', b'data3'])
        mock_response.headers = {"content-length": '15'}
        mock_requests_get.return_value = mock_response
        mock_open.return_value.write.return_value = 15

        # Call the function
        _download_with_progress_bar(url, file_path)

        # Assertions to ensure the function works correctly without content-length header
        mock_requests_get.assert_called_once_with(url, stream=True)
        mock_open.assert_called_once_with(file_path, 'wb')
        
        mock_tqdm.assert_called_once()
        handle = mock_open()
        handle.write.assert_has_calls([unittest.mock.call(b'data1'), unittest.mock.call(b'data2'), unittest.mock.call(b'data3')])
        
    def test_parameter_name_change(self):
        parameters = inspect.signature(_download_with_progress_bar).parameters
        self.assertNotIn('fname', parameters)
        self.assertIn("file_path", parameters)
        self.assertEqual(list(parameters)[1], "file_path")

    def test_function_name_change(self):
        import download
        self.assertTrue(callable(_download_with_progress_bar))
        self.assertNotIn("download", download.__dict__)
      

if __name__ == '__main__':
    unittest.main()
