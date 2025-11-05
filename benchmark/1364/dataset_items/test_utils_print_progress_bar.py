import inspect
import ast
import re
import unittest
from unittest.mock import patch
from io import StringIO
import sys

from ctx_utils import print_progress_bar

class TestPrintProgressBar(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(print_progress_bar)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

        # Create a string buffer to capture the printed output
        self.stdout = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.stdout


    def tearDown(self):
        # Reset the stdout after tests
        sys.stdout = self.original_stdout

    def test_progress_bar_output(self):
        # Test the progress bar output for a full iteration
        items = list(range(0, 11))
        for item in items:
            print_progress_bar(item, 10, prefix='Progress:', suffix='Complete', length=20)
        # Check if the last line is the complete bar
        last_line = self.stdout.getvalue().splitlines()[-1]
        self.assertIn('100.0% Complete', last_line)

    def test_progress_bar_prefix_suffix(self):
        # Test the prefix and suffix in the output
        items = list(range(0, 6))
        for item in items:
            print_progress_bar(item, 5, prefix='Starting:', suffix='Ending', length=20)
        # Get the output lines
        output_lines = self.stdout.getvalue().splitlines()
        # Check if the prefix and suffix are correct
        self.assertTrue(output_lines[1].startswith('Starting:'))
        self.assertTrue(output_lines[-1].endswith('Ending'))

    def test_progress_bar_decimals(self):
        # Test the number of decimal places in the percentage
        items = list(range(0, 2))
        for item in items:
            print_progress_bar(item, 1, decimals=2, length=20)
        # Get the last output line
        last_line = self.stdout.getvalue().splitlines()[-1]
        # Check if the percentage has two decimal places
        self.assertIn('.00%', last_line)

    def test_progress_bar_fill_character(self):
        # Test the use of a custom fill character
        items = list(range(0, 2))
        for item in items:
            print_progress_bar(item, 1, fill='=', length=20)
        # Get the last output line
        last_line = self.stdout.getvalue().splitlines()[-1]
        # Check if the fill character is used in the bar
        self.assertTrue(last_line.startswith(' |==='))

    def test_progress_bar_length(self):
        # Test the length of the progress bar
        items = list(range(0, 2))
        for item in items:
            print_progress_bar(item, 1, fill='=', length=10)
        # Get the last output line
        last_line = self.stdout.getvalue().splitlines()[-1]
        # Check if the bar length is 10 characters
        self.assertEqual(len(last_line.split('|')[1]), 10)

    def test_rename_function(self):
        import ctx_utils
        self.assertTrue(callable(print_progress_bar))
        self.assertNotIn('printProgressBar', ctx_utils.__dict__)

    def test_add_new_parameter(self):
        parameters = inspect.signature(print_progress_bar).parameters
        self.assertIn('print_end', parameters)
        self.assertEqual(parameters['print_end'].default, '\r')

    def test_update_fill_parameter(self):
        parameters = inspect.signature(print_progress_bar).parameters
        self.assertEqual(parameters['fill'].default, '█')

    def test_update_print_statement(self):
        matched_old = re.search(r'[\'\"].+[\'\"]\s*%\s*\(.*\)', self.source, re.DOTALL)
        matched_new = re.search(r'f[\'\"].*{.+}.*[\'\"]', self.source, re.DOTALL)
        self.assertFalse(matched_old)
        self.assertTrue(matched_new)

    @patch('sys.stdout.flush')
    def test_remove_flush(self, mock_flush):
        items = list(range(0, 2))
        for item in items:
            print_progress_bar(item, 1, decimals=2, length=20)
        mock_flush.assert_not_called()

    def test_update_variable_naming(self):
        matched_old = re.search(r'\bfilledLength\b', self.source)
        matched_new = re.search(r'\bfilled_length\b', self.source)
        self.assertFalse(matched_old)
        self.assertTrue(matched_new)

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