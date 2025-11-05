import unittest
from fastapi import Form
from pydantic import BaseModel
import inspect
import asyncio
import ast
import re

# 确保 _base.py 文件在测试脚本所在的目录中
from _base import as_form

# 定义一个用于测试的Pydantic模型
@as_form
class ExampleModel(BaseModel):
    name: str
    age: int

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

class TestAsForm(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(as_form)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_as_form_method_exists(self):
        self.assertTrue(hasattr(ExampleModel, 'as_form'))

    def test_as_form_method_signature(self):
        params = list(inspect.signature(ExampleModel.as_form).parameters.values())
        self.assertEqual(len(params), 2)
        self.assertEqual(params[0].name, 'name')
        self.assertEqual(params[1].name, 'age')
        self.assertTrue(params[0].default is not inspect.Parameter.empty)
        self.assertTrue(params[1].default is not inspect.Parameter.empty)
        self.assertEqual(params[0].annotation, str)
        self.assertEqual(params[1].annotation, int)

    def test_method_signature(self):
        annotations = as_form.__annotations__
        self.assertNotIn('cls', annotations)

    def test_as_form_functionality(self):
        data = {'name': 'John', 'age': 30}
        loop = asyncio.get_event_loop()
        form_instance = loop.run_until_complete(ExampleModel.as_form(**data))
        self.assertEqual(form_instance.name, 'John')
        self.assertEqual(form_instance.age, 30)

    def test_string_updates(self):
        matched_old = re.search(r'cls\.__fields__\.items\(\)', self.source)
        matched_new = re.search(r'cls\.__fields__\.values\(\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

if __name__ == '__main__':
    unittest.main()
