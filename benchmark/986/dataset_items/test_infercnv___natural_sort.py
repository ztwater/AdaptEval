import re, ast, inspect
import typing
import unittest

from infercnv_ import _natural_sort

class TestNaturalSort(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(_natural_sort)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_mixed_case(self):
        lst = ["apple", "banana", "123", "Cherry", "456"]
        expected = ['123', '456', 'apple', 'banana', 'Cherry']
        result = _natural_sort(lst)
        self.assertEqual(result, expected)
        
    def test_only_numbers(self):
        lst = ["1", "2", "3", "4", "5"]
        expected = ['1', '2', '3', '4', '5']
        result = _natural_sort(lst)
        self.assertEqual(result, expected)
        
    def test_only_letters(self):
        lst = ["a", "b", "c", "d", "e"]
        expected = ['a', 'b', 'c', 'd', 'e']
        result = _natural_sort(lst)
        self.assertEqual(result, expected)
        
    def test_special_characters(self):
        lst = ["a1", "b2", "c3", "d4", "e5"]
        expected = ['a1', 'b2', 'c3', 'd4', 'e5']
        result = _natural_sort(lst)
        self.assertEqual(result, expected)
        
    def test_empty_list(self):
        result = _natural_sort([])
        self.assertEqual(result, [])
        
    def test_wrong_parameter_type(self):
        lst = 12345
        with self.assertRaises(TypeError):
            _natural_sort(lst)

    def test_add_type_annotations(self):
        annotations = _natural_sort.__annotations__
        self.assertIn('lst', annotations)
        self.assertTrue(annotations['lst'], typing.Sequence)

    def test_rename_function(self):
        from infercnv_ import _natural_sort
        self.assertTrue(callable(_natural_sort))

    def test_convert_lambda_to_function(self):
        matched_old = re.search(r'\blambda\b', self.source)
        matched_func_convert = re.search(r'\sdef\s+convert\(', self.source)
        matched_func_alphanum = re.search(r'\sdef\s+alphanum_key\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_func_convert)
        self.assertIsNotNone(matched_func_alphanum)

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

