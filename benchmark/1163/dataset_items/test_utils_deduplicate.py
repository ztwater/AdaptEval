import unittest
from typing import List
from ctx_utils import deduplicate
import ast
import re
import inspect

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

class TestDeduplicate(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(deduplicate)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_basic_functionality(self):
        self.assertEqual(deduplicate(['apple', 'banana', 'apple', 'orange', 'banana']), ['apple', 'banana', 'orange'])
    
    def test_empty_list(self):
        self.assertEqual(deduplicate([]), [])
    
    def test_single_element(self):
        self.assertEqual(deduplicate(['apple']), ['apple'])
    
    def test_no_duplicates(self):
        self.assertEqual(deduplicate(['apple', 'banana', 'orange']), ['apple', 'banana', 'orange'])
    
    def test_all_duplicates(self):
        self.assertEqual(deduplicate(['apple', 'apple', 'apple']), ['apple'])
    
    def test_case_sensitivity(self):
        self.assertEqual(deduplicate(['Apple', 'apple']), ['Apple', 'apple'])
    
    def test_large_input(self):
        large_list = ['a'] * 1000 + ['b'] * 1000
        self.assertEqual(deduplicate(large_list), ['a', 'b'])
    
    def test_order_preservation(self):
        self.assertEqual(deduplicate(['b', 'a', 'c', 'a', 'b', 'c']), ['b', 'a', 'c'])

    def test_rename_function(self):
        from ctx_utils import deduplicate
        self.assertTrue(callable(deduplicate))

    def test_add_type_annotations(self):
        annotations = deduplicate.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], List[str])
        self.assertEqual(annotations['seq'], List[str])

    def test_string_updates(self):
        matched_old = re.search(r'seen_add ', self.source)
        matched_new = re.search(r'seen.add\(x\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)


if __name__ == '__main__':
    unittest.main()