import unittest
from unittest.mock import patch
import re, ast, inspect
import math
import random

from ctx_utils import random_range


class TestRandomRange(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(random_range)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_handle_empty_range(self):
        """Test behavior when range is empty."""
        result = list(random_range(0))
        self.assertEqual(result, [])

    def test_handle_default_parameters(self):
        """Test handling of default parameters."""
        result = list(random_range(5))
        expected = [0, 1, 2, 3, 4]
        result.sort()
        expected.sort()
        self.assertEqual(result, expected)

    def test_range_length(self):
        result = list(random_range(10))
        self.assertEqual(len(result), 10)

    @patch('random.randint', return_value=0)
    def test_add_early_return(self, mock_randint):
        list(random_range(0))
        mock_randint.assert_not_called()

    def test_refactor_parameter_handling(self):
        matched_old = re.search(r'==\s*None', self.source)
        matched_new = re.search(r'is\s+None', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_update_max_calculation(self):
        result = list(random_range(0, 3, 2))
        self.assertEqual(len(result), 2)


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
