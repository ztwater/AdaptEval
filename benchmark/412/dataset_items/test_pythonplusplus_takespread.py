import unittest
import inspect
import ast
import re

from pythonplusplus import takespread


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


class TestTakespread(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(takespread)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_takespread_uses_math_ceil(self):
        sequence = [1, 2, 3, 4, 5]
        num = 2
        result = list(takespread(sequence, num))
        expected = [1, 4]
        self.assertEqual(result, expected)

    def test_takespread_even_distribution(self):
        sequence = list(range(10))
        num = 5
        result = list(takespread(sequence, num))
        expected = [0, 2, 4, 6, 8]
        self.assertEqual(result, expected)

    # def test_takespread_more_elements(self):
    #     sequence = list(range(10))
    #     num = 15
    #     result = list(takespread(sequence, num))
    #     expected = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
    #     self.assertEqual(result, expected)

    def test_takespread_less_elements(self):
        sequence = list(range(10))
        num = 3
        result = list(takespread(sequence, num))
        expected = [0, 4, 7]
        self.assertEqual(result, expected)

    def test_takespread_single_element(self):
        sequence = list(range(10))
        num = 1
        result = list(takespread(sequence, num))
        expected = [0]
        self.assertEqual(result, expected)

    # def test_takespread_empty_sequence(self):
    #     sequence = []
    #     num = 5
    #     result = list(takespread(sequence, num))
    #     expected = []
    #     self.assertEqual(result, expected)

    def test_change_api_alias(self):
        matched_old = re.search(r'[^.]ceil\(', self.source)
        matched_new = re.search(r'\bmath\.ceil\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

if __name__ == '__main__':
    unittest.main()

