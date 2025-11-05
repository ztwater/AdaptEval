import unittest
import unittest.mock
from helper import wrap_object
from collections.abc import Callable, Generator
from unittest.mock import MagicMock
import inspect
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
        if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body[0].value.value = ""
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Skip over async function decorators
        node.decorator_list = []
        if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body[0].value.value = ""
        self.generic_visit(node)

class TestWrapObject(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(wrap_object)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_wrap_object(self):
        # Define a test class with an attribute to be wrapped
        class TestClass:
            def __init__(self):
                self.counter = 0

            def increment(self):
                self.counter += 1
                return self.counter

        # Create an instance of the test class
        test_instance = TestClass()

        with wrap_object(test_instance, 'increment') as mock_increment:
            self.assertEqual(TestClass.increment(test_instance), 1)

        with wrap_object(test_instance, 'increment', include_instance=True) as mock_increment:
            self.assertEqual(TestClass.increment(test_instance), 2)

        self.assertEqual(test_instance.increment(), 3)


    def test_add_parameter(self):
        parameters = inspect.signature(wrap_object).parameters
        self.assertIn('include_instance', parameters)
        self.assertEqual(list(parameters)[2], 'include_instance')
        self.assertEqual(parameters['include_instance'].default, False)

    def test_add_type_annotations(self):
        annotations = wrap_object.__annotations__
        self.assertEqual(annotations['include_instance'], bool)

    def test_return_type_annotations(self):
        matched_old = re.search(r'typing\.Generator', self.source)
        matched_new = re.search(r'[^.]Generator', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_update_magicmock(self):
        matched_old = re.search(r'unittest\.mock\.MagicMock', self.source)
        matched_new = re.search(r'[^.]MagicMock', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_mock_include_attribute_annotations(self):
        matched_new_0 = re.search(r'if\s+include_instance:', self.source)
        matched_new_1 = re.search(r'mock(\.__call__)?\(self.+\)', self.source, re.DOTALL)
        self.assertIsNotNone(matched_new_0)
        self.assertIsNotNone(matched_new_1)


if __name__ == '__main__':
    unittest.main()