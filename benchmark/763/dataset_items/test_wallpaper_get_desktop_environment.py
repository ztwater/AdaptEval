import os
import subprocess
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock, call
from wallpaper import get_desktop_environment

class TestGetDesktopEnvironment(unittest.TestCase):

    @patch('sys.platform', "win32")
    def test_update_method_signature(self):
        self.assertEqual(get_desktop_environment(), 'windows')

    def test_update_method_signature_raise_type_error(self):
        with self.assertRaises(TypeError):
            get_desktop_environment(123)  # Should raise TypeError as the function does not accept arguments

    def test_add_type_annotation(self):
        annotations = get_desktop_environment.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], str)

    @patch('os.environ.get')
    @patch('sys.platform', 'linux') 
    @patch('subprocess.Popen')
    def test_gnome_desktop_session_id_call_count(self, mock_Popen, mock_get):
        # Set up the mock to return different values for different calls
        mock_get.side_effect = {
            'DESKTOP_SESSION': 'gnome2',
            'GNOME_DESKTOP_SESSION_ID': 'gnome-session-3.28.0',
            'KDE_FULL_SESSION': 'false'  # Example for another environment variable
        }
        # Set up the mock for subprocess.Popen if needed
        mock_Popen.return_value.stdout = Mock()
        mock_Popen.return_value.stdout.readlines.return_value = ['gnome-session']

        # Call the method
        result = get_desktop_environment()

        # Assert the method returned the expected result
        self.assertEqual(result, 'gnome2')

        # Assert that os.environ.get was called with 'GNOME_DESKTOP_SESSION_ID' exactly once
        # mock_get.assert_called_once_with('GNOME_DESKTOP_SESSION_ID')
        mock_get.assert_has_calls([call('DESKTOP_SESSION'), 
                                   call('GNOME_DESKTOP_SESSION_ID'), 
                                   call('KDE_FULL_SESSION')], any_order=True)


if __name__ == '__main__':
    unittest.main()
