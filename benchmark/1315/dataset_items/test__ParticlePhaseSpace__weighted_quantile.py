import inspect
import re, ast
import unittest
import numpy as np
from _ParticlePhaseSpace import PhaseSpace

class TestWeightedQuantile(unittest.TestCase):

    def setUp(self):
        self.obj = PhaseSpace()
        source = inspect.getsource(PhaseSpace)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_method_signature_with_self(self):
        values = np.array([1, 2, 3, 4])
        quantiles = [0.25, 0.5, 0.75]
        sample_weight = np.array([1, 1, 1, 1])
        result = self.obj._weighted_quantile(values, quantiles, sample_weight)
        expected = np.interp(quantiles,
                             np.cumsum(sample_weight) / np.sum(sample_weight) - 0.5 * sample_weight / np.sum(sample_weight),
                             values)
        np.testing.assert_array_almost_equal(result, expected)

    def test_change_function_type(self):
        from _ParticlePhaseSpace import PhaseSpace
        self.assertTrue(hasattr(PhaseSpace, '_weighted_quantile'))

    def test_remove_unused_parameters(self):
        parameters = inspect.signature(PhaseSpace._weighted_quantile).parameters
        self.assertEqual(len(parameters), 4)
        self.assertNotIn("values_sorted", parameters)
        self.assertNotIn("old_style", parameters)

    def test_remove_sorting_check(self):
        matched_old = re.search(r'if\s+not\s+values_sorted\s*:', self.source)
        self.assertIsNone(matched_old)

    def test_remove_old_style_logic(self):
        matched_old = re.search(r'if\s+old_style\s*:', self.source)
        self.assertIsNone(matched_old)


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
