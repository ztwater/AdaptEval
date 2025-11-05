import unittest
from unittest.mock import patch, MagicMock, call
from io import BytesIO, TextIOWrapper, StringIO, BufferedRandom
from tempfile import TemporaryFile
import os
import sys
import re
import ast
import inspect

import imgcat
from imgcat import _read_binary_stdin


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

 
tmp_dict = {}

def setTmpf(tm): 
    tmp_dict['tempFile'] = tm
    tmp_dict['tempBuffer'] = BufferedRandom(tm)
    tmp_dict['tempIOPort'] = TextIOWrapper(tmp_dict['tempBuffer'] ) 
 

class TestReadBinaryStdin(unittest.TestCase):
    
    def setUp(self):
        source = inspect.getsource(_read_binary_stdin)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)  
        setTmpf(TemporaryFile()) 

    def tearDown(self) -> None:
        tmp_dict['tempIOPort'].close()

    def get_stdin(self):
        return self.tmp    
    
    def test_func_wrap_name(self):
        self.assertTrue(callable(_read_binary_stdin))
        
    def test_vision_var_rename(self):
        matched_old = re.search(r'PY3K\s*=', self.source)
        matched_new = re.search(r'PY3\s*=', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)
    
    @patch('sys.stdin', new_callable=lambda: tmp_dict['tempIOPort'])
    def test_read_binary_stdin_python3(self, mock_stdin):
        tmp = tmp_dict['tempIOPort']
        tmp.write('This is a test')
        tmp.seek(0)
        
        result = _read_binary_stdin()
        self.assertEqual(result, b'This is a test')

    @patch('os.O_BINARY', None, create=True)

    @patch('sys.stdin', new_callable=lambda: tmp_dict['tempIOPort'])
    @patch('sys.platform', 'win32')
    @patch('sys.version_info', (2, 9))
    def test_read_binary_stdin_python2_windows(self, mock_stdin):
        tmp = tmp_dict['tempIOPort']
        tmp.write('This is a test')
        tmp.seek(0)
        mock_msvcrt = MagicMock()
        mock_setmode = MagicMock()
        mock_msvcrt.setmode = mock_setmode

        with patch.dict(imgcat.__dict__, {'msvcrt': mock_msvcrt}):
            with patch('builtins.__import__', side_effect=mock_setmode(42)):
                result = _read_binary_stdin()
                mock_setmode.assert_called_with(42)
                self.assertEqual(result, 'This is a test')

    
if __name__ == '__main__':
     unittest.main()
