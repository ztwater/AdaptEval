import unittest
from unittest.mock import patch, MagicMock
import subprocess
import ast
import re
import inspect

from sge_submit import output_shell


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


class TestOutputShell(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(output_shell)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    @patch('sge_submit.subprocess.Popen')
    def test_popen_called_with_correct_arguments(self, mock_popen):
        # Arrange
        command = 'echo Hello, World'
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        mock_process.communicate.return_value = (b'Hello, World\n', b'')
        mock_process.returncode = 0

        # Act
        result = output_shell(command)

        # Assert
        mock_popen.assert_called_with(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.assertEqual(result, b'Hello, World\n')


    @patch('sge_submit.subprocess.Popen')
    def test_shell_command_fails(self, mock_popen):
        # Arrange
        command = 'exit 1'
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        mock_process.communicate.return_value = (b'', b'Error')
        mock_process.returncode = 1

        # Act
        with patch('builtins.print') as mock_print:
            result = output_shell(command)

        # Assert
        mock_print.assert_any_call("Shell command failed to execute")
        mock_print.assert_any_call(command)
        self.assertIsNone(result)

    @patch('sge_submit.subprocess.Popen')
    def test_os_error_handling(self, mock_popen):
        # Arrange
        command = 'invalid command'
        mock_popen.side_effect = OSError

        # Act
        result = output_shell(command)

        # Assert
        self.assertIsNone(result)

    @patch('sge_submit.subprocess.Popen')
    def test_value_error_handling(self, mock_popen):
        # Arrange
        command = 'invalid command'
        mock_popen.side_effect = ValueError

        # Act
        result = output_shell(command)

        # Assert
        self.assertIsNone(result)
        
    @patch('sge_submit.subprocess.Popen')
    def test_output_is_bytes_not_str(self, mock_popen):
        # Arrange
        command = 'echo Hello, World'
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        mock_process.communicate.return_value = (b'Hello, World\n', b'')
        mock_process.returncode = 0

        # Act
        result = output_shell(command)

        # Assert
        self.assertEqual(result, b'Hello, World\n')
        self.assertIsInstance(result, bytes)

    def test_replace_popen(self):
        matched_old = re.search(r'[^.]Popen\(', self.source)
        matched_new = re.search(r'\bsubprocess\.Popen\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_replace_pipe(self):
        matched_old = re.search(r'[^.]PIPE\b', self.source)
        matched_new = re.search(r'\bsubprocess\.PIPE\b', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_update_print(self):
        matched_old = re.search(r'\bprint\s+"', self.source)
        matched_new = re.search(r'\bprint\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    @patch('sge_submit.subprocess.Popen')
    def test_add_print(self, mock_popen):
        # Arrange
        command = 'exit 1'
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        mock_process.communicate.return_value = (b'', b'Error')
        mock_process.returncode = 1

        # Act
        with patch('builtins.print') as mock_print:
            result = output_shell(command)

        # Assert
        mock_print.assert_any_call(command)

    def test_remove_str_conversion(self):
        matched_old = re.search(r'return\s+str\(output\)', self.source)
        matched_new = re.search(r'return\s+output', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

if __name__ == '__main__':
    unittest.main()
