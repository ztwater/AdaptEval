import unittest
import re
import ast
import inspect
from typing import List

from check_table import camel_case_split
 

class TestCamelCaseSplit(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(camel_case_split)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_add_type_annotations(self):
        annotations = camel_case_split.__annotations__
        self.assertIn('identifier', annotations)
        self.assertEqual(annotations['identifier'], str)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], List[str])

    def test_change_referenced_api_name(self):
        matched_old = re.search(r'[^.]finditer\(', self.source)
        matched_new = re.search(r'\bre.finditer\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_single_word(self):
        result = camel_case_split("Camel")
        self.assertEqual(result, ["Camel"])

    def test_multiple_words(self):
        result = camel_case_split("CamelCaseSplitFunction")
        self.assertEqual(result, ["Camel", "Case", "Split", "Function"])

    def test_acronyms(self):
        result = camel_case_split("HTTPResponseCode")
        self.assertEqual(result, ["HTTP", "Response", "Code"])


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


if __name__ == "__main__":
    unittest.main()
