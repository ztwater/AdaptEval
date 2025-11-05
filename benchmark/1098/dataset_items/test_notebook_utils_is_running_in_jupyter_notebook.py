import re
import unittest
from unittest.mock import patch
import ast
import inspect

from notebook_utils import is_running_in_jupyter_notebook


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


class TestIsRunningInJupyterNotebook(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(is_running_in_jupyter_notebook)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    @patch('IPython.get_ipython')
    def test_jupyter_notebook(self, mock_get_ipython):
        mock_get_ipython.return_value.__class__.__name__ = 'ZMQInteractiveShell'
        self.assertTrue(is_running_in_jupyter_notebook())

    @patch('IPython.get_ipython')
    def test_terminal_ipython(self, mock_get_ipython):
        mock_get_ipython.return_value.__class__.__name__ = 'TerminalInteractiveShell'
        self.assertFalse(is_running_in_jupyter_notebook())

    @patch('IPython.get_ipython')
    def test_other_shell(self, mock_get_ipython):
        mock_get_ipython.return_value.__class__.__name__ = 'OtherShell'
        self.assertFalse(is_running_in_jupyter_notebook())

    def test_rename_method(self):
        pass
        
    def test_import_statement(self):
        matched_import = re.search(r'import\s+IPython\.get_ipython|'
                                   r'from\s+IPython\s+import\s+get_ipython',
                                   self.source)
        self.assertIsNotNone(matched_import)

    @patch('IPython.get_ipython', side_effect=ImportError)
    def test_update_exception_type(self, mock_get_ipython):
        self.assertFalse(is_running_in_jupyter_notebook())


if __name__ == '__main__':
    unittest.main()
