import unittest
import re
import ast
import inspect
import numpy as np
from angles_and_coords import angle_between


class TestAngleBetween(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(angle_between)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_angle_between(self):
        # Test cases to verify the correctness of the function
        self.assertAlmostEqual(angle_between(np.array([1, 0, 0]), np.array([0, 1, 0])), np.pi / 2)
        self.assertAlmostEqual(angle_between(np.array([1, 0, 0]), np.array([1, 0, 0])), 0.0)
        self.assertAlmostEqual(angle_between(np.array([1, 0, 0]), np.array([-1, 0, 0])), np.pi)
        self.assertAlmostEqual(angle_between(np.array([1, 2, 3]), np.array([4, 5, 6])), 0.2257261285527342)
        self.assertAlmostEqual(angle_between(np.array([1, 0]), np.array([0, 1])), np.pi / 2)
        self.assertAlmostEqual(angle_between(np.array([1, 0]), np.array([1, 0])), 0.0)
        self.assertAlmostEqual(angle_between(np.array([1, 0]), np.array([-1, 0])), np.pi)

    def test_type_annotations(self):
        # Test to ensure type annotations are correct
        from typing import get_type_hints
        hints = get_type_hints(angle_between)
        self.assertEqual(hints['v1'], np.ndarray)
        self.assertEqual(hints['v2'], np.ndarray)
        self.assertEqual(hints['return'], float)

    def test_inline_unit_vector_function(self):
        import angles_and_coords
        self.assertNotIn('unit_vector', angles_and_coords.__dict__)

        matched_unit_vec = re.search(r'unit_vector\s*=\s*lambda', self.source)
        self.assertIsNotNone(matched_unit_vec)


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

if __name__ == '__main__':
    unittest.main()
