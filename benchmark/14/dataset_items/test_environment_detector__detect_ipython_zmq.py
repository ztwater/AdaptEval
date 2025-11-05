# import sys
# import os
# root_path = os.path.join('', *os.path.split(os.path.abspath(__file__))[:-2])
# sys.path.append(root_path)
import inspect
import re

from environment_detector import _detect_ipython_zmq

import unittest
from unittest.mock import patch, MagicMock

class TestDetectIpythonZmq(unittest.TestCase):

    @patch('IPython.get_ipython')
    def test_in_ipython_zmq_shell(self, mock_get_ipython):
        # Setup mock to simulate being in ZMQInteractiveShell
        mock_shell = MagicMock()
        mock_shell.__class__.__name__ = 'ZMQInteractiveShell'
        mock_get_ipython.return_value = mock_shell

        self.assertTrue(_detect_ipython_zmq())

    @patch('IPython.get_ipython')
    def test_in_ipython_terminal_shell(self, mock_get_ipython):
        # Setup mock to simulate being in TerminalInteractiveShell
        mock_shell = MagicMock()
        mock_shell.__class__.__name__ = 'TerminalInteractiveShell'
        mock_get_ipython.return_value = mock_shell

        self.assertFalse(_detect_ipython_zmq())

    @patch('IPython.get_ipython')
    def test_in_standard_python_interpreter(self, mock_get_ipython):
        # Setup mock to simulate NameError (no IPython environment)
        mock_get_ipython.side_effect = NameError

        self.assertFalse(_detect_ipython_zmq())

    @patch('IPython.get_ipython')
    def test_in_unknown_ipython_environment(self, mock_get_ipython):
        # Setup mock to simulate an unknown IPython environment
        mock_shell = MagicMock()
        mock_shell.__class__.__name__ = 'UnknownShell'
        mock_get_ipython.return_value = mock_shell

        self.assertFalse(_detect_ipython_zmq())

    def test_rename_method(self):
        _detect_ipython_zmq()

    def test_add_imports(self):
        source = inspect.getsource(_detect_ipython_zmq)
        matched_import = re.search(r'import\s+IPython\.get_ipython|'
                                   r'from\s+IPython\s+import\s+get_ipython',
                                   source)
        self.assertIsNotNone(matched_import)

if __name__ == '__main__':
    unittest.main()

