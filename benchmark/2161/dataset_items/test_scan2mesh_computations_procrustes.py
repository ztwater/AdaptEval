import unittest
import numpy as np
from scan2mesh_computations import procrustes
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
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Skip over async function decorators
        node.decorator_list = []
        self.generic_visit(node)

class TestProcrustes(unittest.TestCase):

    def setUp(self):
        source = inspect.getsource(procrustes)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)
        self.X = np.array([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ])
        self.Y = np.array([
            [4.0, 5.0],
            [6.0, 7.0],
            [8.0, 9.0]
        ])

    def test_reflection_best(self):
        """Test reflection logic when reflection='best'"""
        expected_rotation = np.array([[1.0, 0.0], [0.0, 1.0]])
        expected_translation = np.array([-3.0, -3.0])
        d, Z, tform = procrustes(self.X, self.Y, reflection='best')
        self.assertEqual(d, 0.0)
        np.testing.assert_array_almost_equal(Z, self.X)
        np.testing.assert_array_almost_equal(tform['rotation'], expected_rotation)
        self.assertAlmostEqual(tform['scale'], 1.0)
        np.testing.assert_array_almost_equal(tform['translation'], expected_translation)

    def test_reflection_true(self):
        """Test reflection logic when reflection=True"""
        expected_rotation = np.array([[0.0, 1.0], [1.0, 0.0]])
        expected_translation = np.array([-4.0, -2.0])
        d, Z, tform = procrustes(self.X, self.Y, reflection=True)
        self.assertEqual(d, 0.0)
        np.testing.assert_array_almost_equal(Z, self.X)
        np.testing.assert_array_almost_equal(tform['rotation'], expected_rotation)
        self.assertAlmostEqual(tform['scale'], 1.0)
        np.testing.assert_array_almost_equal(tform['translation'], expected_translation)

    def test_scaling_false(self):
        new_Y = np.array([[4.0, 6.0],
                          [6.0, 9.0],
                          [8.0, 10.0]])
        expected_Z = np.array([[1.0, 1.6667],
                               [3.0, 4.6667],
                               [5.0, 5.6667]])
        expected_rotation = np.array([[1.0, 0.0], [0.0, 1.0]])
        expected_translation = np.array([-3.0, -4.3333])
        d, Z, tform = procrustes(self.X, new_Y, scaling=False, reflection='best')
        self.assertAlmostEqual(d, 0.0417, places=3)
        np.testing.assert_array_almost_equal(Z, expected_Z, decimal=1e-3)
        np.testing.assert_array_almost_equal(tform['rotation'], expected_rotation, decimal=1e-3)
        self.assertAlmostEqual(tform['scale'], 1.0)
        np.testing.assert_array_almost_equal(tform['translation'], expected_translation, decimal=1e-3)

    def test_reflection_comparison(self):
        matched_old = re.search(r'reflection\s*!=\s*[\'\"]best[\'\"]', self.source)
        matched_new = re.search(r'reflection\s+is\s+not\s+[\'\"]best[\'\"]', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

if __name__ == '__main__':
    unittest.main()
