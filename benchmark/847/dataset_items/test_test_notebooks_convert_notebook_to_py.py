import unittest
from unittest.mock import patch, mock_open
from pathlib import Path
import json
import inspect
import re
import ast
import astunparse

# Assume the second snippet is in a module named 'notebook_converter'
from test_notebooks import convert_notebook_to_py

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

class TestConvertNotebookToPy(unittest.TestCase):

    def setUp(self):
        # Set up any prerequisites for the tests, such as creating dummy files
        self.notebook_path = Path('test_notebook.ipynb')
        self.py_path = Path('test_output.py')
        self.notebook_content = {
    "cells": [
        {
            "id": '0',
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [],
            "source": [
                "get_ipython()",
                "\n"
                "print('Hello, world!')"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.11"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}
        with open(self.notebook_path, 'w') as f:
            json.dump(self.notebook_content, f)

        source = inspect.getsource(convert_notebook_to_py)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = astunparse.unparse(tree)
        

    def tearDown(self):
        # Clean up after tests, such as removing dummy files
        if self.notebook_path.exists():
            self.notebook_path.unlink()
        if self.py_path.exists():
            self.py_path.unlink()

    def test_rename_function(self):
        from test_notebooks import convert_notebook_to_py

    def test_convert_notebook_to_py(self):
        convert_notebook_to_py(self.notebook_path, self.py_path)
        self.assertTrue(self.py_path.exists())

        # Read the content of the Python file
        with open(self.py_path, 'r') as f:
            content = f.read()
        self.assertIn("# get_ipython", content)

    def test_string_updates(self):
        matched_utf_8 = re.search(r"encode\.\(\s*'utf-8'\s*\)", self.source)
        self.assertIsNone(matched_utf_8)

    def test_add_type_annotations(self):
        annotations = convert_notebook_to_py.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], None)
        self.assertEqual(annotations['nb_fn'], Path)
        self.assertEqual(annotations['py_fn'], Path)

    def test_import_updates(self):
        matched_nbformat_import = re.search(r'import\s*nbformat', self.source)
        matched_nbconvert_import = re.search(r'from\s*nbconvert\s*import\s*PythonExporter', self.source)
        self.assertIsNotNone(matched_nbformat_import)
        self.assertIsNotNone(matched_nbconvert_import)

    def test_rename_parameters(self):
        parameters = inspect.signature(convert_notebook_to_py).parameters
        self.assertNotIn('notebookPath', parameters)
        self.assertNotIn('modulePath', parameters)
        self.assertIn('nb_fn', parameters)
        self.assertIn('py_fn', parameters)


if __name__ == '__main__':
    unittest.main()