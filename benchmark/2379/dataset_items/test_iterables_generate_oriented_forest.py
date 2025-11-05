import unittest
from iterables import generate_oriented_forest
import inspect
from unittest.mock import patch
import ast
import re

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

class TestGenerateOrientedForest(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(generate_oriented_forest)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)
    
    def test_rename_method(self):
        import iterables
        self.assertTrue(callable(generate_oriented_forest))
        self.assertNotIn('generate_oriented_forest_2', iterables.__dict__)

    @patch('builtins.list', wraps=list)
    def test_initialize_list_with_range(self, patch_list):
        result = [x for x in generate_oriented_forest(4)]
        patch_list.assert_called_once()

    def test_refactor_variable_names(self):
        matched_L = re.search(r'\sL\s', self.source)
        matched_P = re.search(r'\sP\s', self.source)
        self.assertIsNone(matched_L)
        self.assertIsNotNone(matched_P)

    def test_introduce_target_variable(self):
        matched_new = re.search(r'target\s*=\s*P\[\s*p\s*]\s*-\s*1', self.source)
        self.assertIsNotNone(matched_new)

    def test_introduce_offset_variable(self):
        source = inspect.getsource(generate_oriented_forest)
        self.assertIn('offset', source)
        matched_new = re.search(r'offset\s*=\s*p\s*-\s*q', self.source)
        self.assertIsNotNone(matched_new)

    def test_for_while_loop(self):
        matched_old = re.search(r'while\s+i\s*<=\s*n:', self.source)
        matched_new = re.search(r'for\s+\w+\s+in\s+range\(\s*p\s*,\s*n\s*\+\s*1\s*\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_generate_oriented_forest_output(self):
        # Test the output of the function
        expected_output = [
            [0, 1, 2, 3], [0, 1, 2, 2], [0, 1, 2, 1], [0, 1, 2, 0],
            [0, 1, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0]
        ]
        result = list(generate_oriented_forest(4))
        self.assertEqual(result, expected_output)
    
if __name__ == '__main__':
    unittest.main()