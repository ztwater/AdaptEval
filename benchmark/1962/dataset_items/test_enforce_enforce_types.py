import unittest
from unittest.mock import patch
import re
import ast
import inspect
from pydoc import locate
from enforce import enforce_types


# Test function
@enforce_types
def test_func(x: int, y: str) -> str:
    return f"{x} and {y}"

@enforce_types
def test_func_str(x: int, y: 'str') -> str:
    return f"{x} and {y}"

# Test class
@enforce_types
class TestClass:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def concat(self) -> str:
        return f"{self.a} and {self.b}"


class TestEnforceTypes(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(enforce_types)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_correct_types(self):
        # Test with correct types
        self.assertEqual(test_func(1, "hello"), "1 and hello")

        # Test class with correct types
        obj = TestClass(2, "world")
        self.assertEqual(obj.concat(), "2 and world")

    def test_incorrect_types_function(self):
        # Test with incorrect types
        with self.assertRaises(TypeError):
            test_func("one", 2)

    def test_incorrect_types_class(self):
        # Test class with incorrect types
        with self.assertRaises(TypeError):
            TestClass("two", 3)

    def test_missing_annotations(self):
        # Define a function without type annotations
        @enforce_types
        def unannotated_func(x, y):
            return x + y

        # Should not raise despite no annotations
        self.assertEqual(unannotated_func(1, 2), 3)
        self.assertEqual(unannotated_func("1", "2"), "12")

    def test_handle_string_type_hints(self):
        self.assertEqual(test_func_str(1, "hello"), "1 and hello")

    def test_handle_version_specific_type(self):
        matched_sys = re.search(r'\bsys\.version_info\b', self.source)
        matched_get_origin = re.search(r'\b(typing\.)?get_origin\b', self.source)
        self.assertIsNotNone(matched_sys)
        self.assertIsNotNone(matched_get_origin)

    def test_refactor_validity_check(self):
        matched_valid_0 = re.search(r'\bis_valid\b', self.source)
        matched_valid_1 = re.search(r'\bis_valid\s*=', self.source)
        matched_valid_2 = re.search(r'if\s+(not\s+)?is_valid\b', self.source)
        self.assertIsNotNone(matched_valid_0)
        self.assertIsNotNone(matched_valid_1)
        self.assertIsNotNone(matched_valid_2)

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
