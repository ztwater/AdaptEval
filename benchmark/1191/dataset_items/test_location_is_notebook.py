import unittest
from unittest.mock import patch, MagicMock
from location import is_notebook

class TestIsNotebook(unittest.TestCase):
    def test_in_notebook(self):
        with patch('IPython.core.getipython.get_ipython') as mock_get_ipython:
            mock_shell = MagicMock()
            mock_shell.__class__.__name__ = 'ZMQInteractiveShell'
            mock_get_ipython.return_value = mock_shell
            self.assertTrue(is_notebook())

    def test_in_terminal(self):
        with patch('IPython.core.getipython.get_ipython') as mock_get_ipython:
            mock_shell = MagicMock()
            mock_shell.__class__.__name__ = 'TerminalInteractiveShell'
            mock_get_ipython.return_value = mock_shell
            self.assertFalse(is_notebook())

    def test_other_shell(self):
        with patch('IPython.core.getipython.get_ipython') as mock_get_ipython:
            mock_shell = MagicMock()
            mock_shell.__class__.__name__ = 'OtherShell'
            mock_get_ipython.return_value = mock_shell
            self.assertFalse(is_notebook())

    def test_name_error(self):
        with patch('IPython.core.getipython.get_ipython', side_effect=NameError):
            self.assertFalse(is_notebook())

    def test_module_not_found_error(self):
        with patch('builtins.__import__') as mock_import:
            mock_import.side_effect = ModuleNotFoundError("IPython not found")
            self.assertFalse(is_notebook())
            self.assertIn('IPython.core.getipython', mock_import.call_args.args)
    

if __name__ == '__main__':
    unittest.main()