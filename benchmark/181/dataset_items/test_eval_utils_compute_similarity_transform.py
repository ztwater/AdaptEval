import inspect
import re
import unittest
import numpy as np
import ast

from eval_utils import compute_similarity_transform


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


class TestComputeSimilarityTransform(unittest.TestCase):

    def setUp(self):
        source = inspect.getsource(compute_similarity_transform)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)
        self.X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        self.Y = np.array([[2.0, 4.0], [6.0, 8.0], [10.0, 12.0]])

    def test_functional_correctness(self):
        # A4, A5, A8
        # Just a basic call to ensure the function is callable
        # Ensures 'reflection' parameter removal has no unintended side effects
        # Indirectly tested by ensuring the function runs without the shape variables
        d, Z, T, b, c = compute_similarity_transform(self.X, self.Y)
        self.assertIsNotNone(d)
        self.assertIsNotNone(Z)
        self.assertIsNotNone(T)
        self.assertIsNotNone(b)
        self.assertIsNotNone(c)

    def test_rename_method(self):
        compute_similarity_transform(self.X, self.Y)

    def test_add_type_annotations(self):
        annotations = compute_similarity_transform.__annotations__
        expected = {
            'X': np.ndarray,
            'Y': np.ndarray
        }
        self.assertEqual(annotations, expected)

    def test_update_default_parameter(self):
        parameters = inspect.signature(compute_similarity_transform).parameters
        self.assertNotIn('scaling', parameters)
        self.assertIn('compute_optimal_scale', parameters)
        self.assertEqual(parameters['compute_optimal_scale'].default, False)

    def test_delete_default_parameter(self):
        parameters = inspect.signature(compute_similarity_transform).parameters
        self.assertNotIn('reflection', parameters)

    def test_remove_shape_logic(self):
        matched_x_shape = re.search(r'X\.shape', self.source)
        matched_y_shape = re.search(r'Y\.shape', self.source)
        matched_if = re.search(r'if\s+my\s*<\s*m:', self.source)
        matched_concat = re.search(r'np\.concatenate', self.source)
        self.assertIsNone(matched_x_shape)
        self.assertIsNone(matched_y_shape)
        self.assertIsNone(matched_if)
        self.assertIsNone(matched_concat)

    def test_refactor_unit_norm(self):
        matched_inplace_x = re.search(r'X0\s*/=\s*normX', self.source)
        matched_inplace_y = re.search(r'Y0\s*/=\s*normY', self.source)
        matched_sf_x = re.search(r'X0\s*=\s*X0\s*/\s*normX', self.source)
        matched_sf_y = re.search(r'Y0\s*=\s*Y0\s*/\s*normY', self.source)
        self.assertIsNone(matched_inplace_x)
        self.assertIsNone(matched_inplace_y)
        self.assertIsNotNone(matched_sf_x)
        self.assertIsNotNone(matched_sf_y)

    def test_ensure_proper_rotation(self):
        # Ensure proper rotation adjustment logic
        d, Z, T, b, c = compute_similarity_transform(self.X, self.Y)
        detT = np.linalg.det(T)
        self.assertAlmostEqual(detT, 1.0, delta=1e-6)

    def test_compute_optimal_scaling(self):
        # Ensure the logic for computing optimal scaling works
        d, Z, T, b, c = compute_similarity_transform(self.X, self.Y, compute_optimal_scale=True)
        self.assertNotEqual(b, 1)

    def test_return_values(self):
        # Ensure the return values are as expected
        d, Z, T, b, c = compute_similarity_transform(self.X, self.Y)
        self.assertIsNotNone(d)
        # self.assertIsInstance(d, float)
        self.assertIsInstance(Z, np.ndarray)
        self.assertIsInstance(T, np.ndarray)
        self.assertIsNotNone(b)
        # self.assertIsInstance(b, float)
        self.assertIsInstance(c, np.ndarray)


if __name__ == '__main__':
    unittest.main()
