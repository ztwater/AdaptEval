import unittest
from unittest.mock import patch, MagicMock
from joblib import Parallel, delayed
from math import sqrt
from tqdm import tqdm
import re
import ast
import inspect

from convert_text_to_phn import tqdm_joblib

class TestTqdmJoblib(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(tqdm_joblib)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_tqdm_joblib_parallel_execution(self):
        """Test the Parallel execution with tqdm_joblib context manager"""
        with tqdm_joblib(tqdm(total=10)) as progress_bar:
            results = Parallel(n_jobs=1)(delayed(sqrt)(i ** 2) for i in range(10))
            self.assertEqual(len(results), 10)
            self.assertTrue(all(isinstance(result, float) for result in results))
            self.assertEqual(progress_bar.n, 10)
            self.assertEqual(progress_bar.n, progress_bar.total)

    def test_change_referenced_api_name(self):
        matched_ori = re.search(r'\bjoblib\.parallel\.', self.source)
        matched_new = re.search(r'[^.\w]parallel\.', self.source)
        self.assertIsNone(matched_ori)
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