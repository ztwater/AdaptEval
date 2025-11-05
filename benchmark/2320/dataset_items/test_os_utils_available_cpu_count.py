import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import re
import ast
import inspect

from os_utils import available_cpu_count

class TestAvailableCpuCount(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(available_cpu_count)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_add_return_type_annotation(self):
        annotations = available_cpu_count.__annotations__
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], int)

    @patch('builtins.bin', return_value="111111")
    def test_cpuset(self, mock_bin):
        mock_open = MagicMock()
        mock_open.read = MagicMock(return_value="")
        mock_search = MagicMock()
        mock_search.group = MagicMock(return_value="1")
        with patch('builtins.open', return_valu=mock_open):
            with patch('re.search', return_value=mock_search):
                result = available_cpu_count()
                self.assertEqual(result, 6)

    @patch('multiprocessing.cpu_count', return_value=42)
    @patch('re.search', side_effect=IOError)
    def test_multiprocessing(self, mock_search, mock_cpu_count):
        result = available_cpu_count()
        mock_cpu_count.assert_called()
        self.assertEqual(result, 42)

    @patch('psutil.cpu_count', return_value=42)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_psutil_cpu_count(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count):
        result = available_cpu_count()
        self.assertEqual(result, 42)

    @patch('os.sysconf', return_value=42)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_posix(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf):
        result = available_cpu_count()
        self.assertEqual(result, 42)

    @patch('os.sysconf', side_effect=ValueError)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_windows(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf):
        with patch.dict(os.environ, {"NUMBER_OF_PROCESSORS": '42'}):
            result = available_cpu_count()
            self.assertEqual(result, 42)

    @patch.dict(os.environ, {"NUMBER_OF_PROCESSORS": '-1'})
    @patch('os.sysconf', side_effect=ValueError)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_bsd(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf):
        mock_popen = MagicMock()
        mock_popen.communicate = MagicMock(return_value=[42])
        with patch('subprocess.Popen', return_value=mock_popen):
            result = available_cpu_count()
            self.assertEqual(result, 42)

    @patch.dict(os.environ, {"NUMBER_OF_PROCESSORS": '-1'})
    @patch('os.sysconf', side_effect=ValueError)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_linux(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf):
        mock_open = MagicMock()
        mock_open.read = MagicMock(return_value="processor\t: 0\nprocessor\t: 1\nprocessor\t: 2\n")
        with patch('builtins.open', return_value=mock_open):
            result = available_cpu_count()
            self.assertEqual(result, 3)

    @patch('os.listdir', return_value=["cpuid@000", "cpuid@111", "cpuid@222", "cpuid@333"])
    @patch.dict(os.environ, {"NUMBER_OF_PROCESSORS": '-1'})
    @patch('os.sysconf', side_effect=ValueError)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_solaris(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf, mock_listdir):
        mock_open = MagicMock()
        mock_open.read = MagicMock(return_value="")
        with patch('builtins.open', return_value=mock_open):
            result = available_cpu_count()
            self.assertEqual(result, 4)

    @patch('os.listdir', side_effect=OSError)
    @patch.dict(os.environ, {"NUMBER_OF_PROCESSORS": '-1'})
    @patch('os.sysconf', side_effect=ValueError)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_other_unixes_normal(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf, mock_listdir):
        mock_open = MagicMock()
        mock_open.read = MagicMock(return_value="\ncpu0:0\ncpu1:1\ncpu2:2\ncpu3:3\ncpu4:4")
        with patch('builtins.open', return_value=mock_open):
            result = available_cpu_count()
            self.assertEqual(result, 5)

    @patch('builtins.open', side_effect=IOError)
    @patch('os.listdir', side_effect=OSError)
    @patch.dict(os.environ, {"NUMBER_OF_PROCESSORS": '-1'})
    @patch('os.sysconf', side_effect=ValueError)
    @patch('psutil.cpu_count', side_effect=ImportError)
    @patch('multiprocessing.cpu_count', side_effect=ImportError)
    @patch('re.search', side_effect=IOError)
    def test_other_unixes_ioerror(self, mock_search, mock_mp_cpu_count, mock_psutil_cpu_count, mock_sysconf, mock_listdir, mock_open):
        mock_popen = MagicMock()
        mock_popen.communicate = MagicMock(return_value=[b'\ncpu0:0\ncpu1:1\ncpu2:2\ncpu3:3\ncpu4:4\ncpu5:5'])
        with patch('subprocess.Popen', return_value=mock_popen):
            result = available_cpu_count()
            self.assertEqual(result, 6)

    def test_delete_jython(self):
        matched_java = re.search(r'(from\s+java\.lang\s+import)|import\s+java(\.lang)?', self.source)
        self.assertIsNone(matched_java)

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
        if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body[0].value.value = ""
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Skip over async function decorators
        node.decorator_list = []
        self.generic_visit(node)

if __name__ == "__main__":
    unittest.main()
