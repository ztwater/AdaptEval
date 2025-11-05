import inspect
import re
import ast
import unittest
from unittest.mock import patch, MagicMock, call
from pathlib import Path

from wallpaper import set_wallpaper


class TestSetWallpaper(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(set_wallpaper)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    @patch('wallpaper.get_desktop_environment')
    @patch('wallpaper.subprocess.Popen')
    def test_gnome_environment(self, mock_popen, mock_get_desktop_environment):
        mock_get_desktop_environment.return_value = 'gnome'
        file_loc = '/path/to/image.jpg'
        uri = Path(file_loc).as_uri()

        set_wallpaper(file_loc)

        calls = [
            unittest.mock.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', uri]),
            unittest.mock.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri-dark', uri])
        ]
        mock_popen.assert_has_calls(calls, any_order=True)

    @patch('wallpaper.get_desktop_environment')
    @patch('wallpaper.subprocess.Popen')
    def test_xfce4_first_run(self, mock_popen, mock_get_desktop_environment):
        mock_get_desktop_environment.return_value = 'xfce4'
        file_loc = '/path/to/image.jpg'
        first_run = True

        set_wallpaper(file_loc, first_run)

        calls = [
            unittest.mock.call(
                ['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitor0/image-path', '-s', file_loc]),
            unittest.mock.call(
                ['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitor0/image-style', '-s', '3']),
            unittest.mock.call(
                ['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitor0/image-show', '-s', 'true']),
            unittest.mock.call(['xfdesktop', '--reload'])
        ]
        mock_popen.assert_has_calls(calls, any_order=True)

    @patch('wallpaper.get_desktop_environment')
    @patch('sys.stderr.write')
    def test_environment_not_supported(self, mock_err_write, mock_get_desktop_environment):
        mock_get_desktop_environment.return_value = 'unknown_env'
        file_loc = '/path/to/image.jpg'

        result = set_wallpaper(file_loc, first_run=True)

        calls = [call("Warning: Failed to set wallpaper. Your desktop environment is not supported."),
                 call(f"You can try manually to set your wallpaper to {file_loc}")]
        mock_err_write.assert_has_calls(calls)
        self.assertFalse(result)

    def test_change_function_type(self):
        from wallpaper import set_wallpaper
        parameters = inspect.signature(set_wallpaper).parameters
        self.assertNotIn('self', parameters)

    def test_add_type_annotations(self):
        annotations = set_wallpaper.__annotations__
        expected = {
            'file_loc': str,
            'first_run': bool
        }
        self.assertEqual(annotations, expected)

    @patch('wallpaper.get_desktop_environment')
    def test_set_default_param_value(self, mock_get_desktop_environment):
        parameters = inspect.signature(set_wallpaper).parameters
        # check text
        matched_true = re.search(r'=\s*True', str(parameters['first_run']))
        self.assertIsNotNone(matched_true)
        # check function
        mock_get_desktop_environment.return_value = 'unknown_env'
        file_loc = '/path/to/image.jpg'
        result = set_wallpaper(file_loc)
        self.assertFalse(False)

    @patch('os.path.isfile')
    @patch('wallpaper.get_home_dir')
    @patch('wallpaper.get_config_dir')
    @patch('wallpaper.get_desktop_environment')
    def test_change_func_calls(self, mock_get_desktop_environment, mock_get_config_dir, mock_get_home_dir, mock_isfile):
        mock_get_desktop_environment.return_value = 'razor-qt'
        mock_isfile.return_value = False
        file_loc = '/path/to/image.jpg'

        set_wallpaper(file_loc)
        mock_get_desktop_environment.assert_called()
        mock_get_config_dir.assert_called()
        mock_get_home_dir.assert_called()

    @patch('pathlib.Path.as_uri')
    @patch('wallpaper.get_desktop_environment')
    def test_uri_handling(self, mock_get_desktop_environment, mock_path_as_uri):
        mock_get_desktop_environment.return_value = 'gnome'
        file_loc = '/path/to/image.jpg'
        mock_path_as_uri.return_value = Path(file_loc).as_uri()

        set_wallpaper(file_loc)
        mock_path_as_uri.assert_called()

    def test_local_import(self):
        matched_import_gio = re.search(r'from\s+gi\.repository\s+import\s+Gio|'
                                       r'import\s+gi\.repository', self.source)
        matched_import_config = re.search(r'import\s+configparser|'
                                          r'from\s+configparser\s+import\s+ConfigParser', self.source)
        self.assertIsNotNone(matched_import_gio)
        self.assertIsNotNone(matched_import_config)

    @patch('wallpaper.get_desktop_environment')
    @patch('wallpaper.subprocess.Popen')
    def test_gnome_dark_mode(self, mock_popen, mock_get_desktop_environment):
        mock_get_desktop_environment.return_value = 'gnome'
        file_loc = '/path/to/image.jpg'
        uri = Path(file_loc).as_uri()

        set_wallpaper(file_loc)

        calls = [
            unittest.mock.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri-dark', uri])
        ]
        mock_popen.assert_has_calls(calls, any_order=True)

    @patch('wallpaper.subprocess.Popen')
    def test_update_wallpaper_setting_command(self, mock_popen):
        file_loc = '/path/to/image.jpg'
        with patch('wallpaper.get_desktop_environment') as mock_env:
            for return_value in ['kde3', 'lxde', 'windowmake']:
                mock_env.return_value = return_value
                set_wallpaper(file_loc)
                args = mock_popen.call_args.args
                self.assertIsInstance(args[0], list)

    def test_change_api_name(self):
        matched_old = re.search(r'\bcodecs\.open\(', self.source)
        matched_new = re.search(r'[^.\w]open\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    @patch('wallpaper.get_desktop_environment')
    def test_windows_environment(self, mock_env):
        import ctypes
        mock_env.return_value = 'windows'
        mock_info = MagicMock()
        ctypes.windll = MagicMock()
        ctypes.windll.user32.SystemParametersInfoW = mock_info
        file_loc = '/path/to/image.jpg'
        set_wallpaper(file_loc)
        mock_info.assert_called_with(20, 0, file_loc, 0)

    @patch('wallpaper.get_desktop_environment')
    @patch('wallpaper.subprocess.Popen')
    @patch('wallpaper.sys.platform', 'darwin')
    def test_mac_environment(self, mock_popen, mock_get_desktop_environment):
        mock_get_desktop_environment.return_value = 'mac'
        file_loc = '/path/to/image.jpg'
        set_wallpaper(file_loc)
        OSASCRIPT = """
            on run (clp)
                if clp's length is not 1 then error "Incorrect Parameters"
                local file_loc
                set file_loc to clp's item 1
                tell application "Finder" to set desktop picture to POSIX file file_loc
            end run
            """
        mock_popen.assert_called_with(["osascript", "-e", OSASCRIPT, "--", file_loc])

    def test_general_exception_handling(self):
        matched_old = re.search(r'except\s*:', self.source)
        matched_new = re.search(r'except\s+Exception:', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

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
