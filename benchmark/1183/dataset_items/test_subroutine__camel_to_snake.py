import unittest
import re
from subroutine import _camel_to_snake
import re
import ast
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

class TestCamelToSnake(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(_camel_to_snake)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)
        # for python version lower than 3.8 using astunparse.unparse
    
    def test_empty_string(self):
        self.assertEqual(_camel_to_snake(''), '')

    def test_no_change_needed(self):
        self.assertEqual(_camel_to_snake('already_snake_case'), 'already_snake_case')

    def test_camel_case(self):
        self.assertEqual(_camel_to_snake('camelCase'), 'camel_case')

    def test_pascal_case(self):
        self.assertEqual(_camel_to_snake('PascalCase'), 'pascal_case')

    def test_mixed_with_numbers(self):
        self.assertEqual(_camel_to_snake('camel2Case'), 'camel2_case')

    def test_acronyms(self):
        self.assertEqual(_camel_to_snake('HTTPResponseCodeXYZ'), 'http_response_code_xyz')

    def test_multiple_uppercase_letters(self):
        self.assertEqual(_camel_to_snake('AAAAA'), 'aaaaa')

    def test_leading_uppercase(self):
        self.assertEqual(_camel_to_snake('CamelCase'), 'camel_case')

    def test_trailing_uppercase(self):
        self.assertEqual(_camel_to_snake('camelCaseX'), 'camel_case_x')

    def test_snake_case_already(self):
        self.assertEqual(_camel_to_snake('snake_case_already'), 'snake_case_already')

    def test_rename_function(self):
        from subroutine import _camel_to_snake
        self.assertTrue(callable(_camel_to_snake))

    def test_lower_adaptations(self):
        matched_old = re.search(r'\bre\.sub\(.+\)\.lower\(\)', self.source, re.DOTALL)
        matched_sub = re.search(r'\bre\.sub\(.+\)\s', self.source, re.DOTALL)
        matched_lower = re.search(r'[^(]\.lower\(\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_sub)
        self.assertIsNotNone(matched_lower)

if __name__ == '__main__':
    unittest.main()