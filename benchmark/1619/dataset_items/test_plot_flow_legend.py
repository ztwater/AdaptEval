import unittest
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.cm as cm
from matplotlib.testing.decorators import image_comparison
from unittest.mock import patch
import re, ast, inspect

from plot import flow_legend


class TestFlowLegend(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(flow_legend)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    # @image_comparison(baseline_images=['flow_legend_plot'], extensions=['png'])
    # def test_flow_legend_plot(self, extension='png'):
    #     # This test will compare the generated plot with a baseline image.
    #     # You need to generate the baseline image first by running the test with the --generate_baseline argument.
    #     flow_legend()

    def test_use_of_correct_function_name(self):
        self.assertTrue(callable(flow_legend))

    @patch('matplotlib.cm.inferno', wraps=cm.inferno)
    @patch('matplotlib.cm.winter', wraps=cm.winter)
    def test_direct_use_of_cm_winter(self, mock_winter, mock_inferno):
        flow_legend()
        mock_winter.assert_called()
        mock_inferno.assert_not_called()

    def test_direct_use_of_np_arctan2(self):
        matched_old = re.search(r'[^.]arctan2\(', self.source)
        matched_new = re.search(r'(np|numpy)\.arctan2\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_removal_of_pivot_argument(self):
        with patch('matplotlib.pyplot.quiver', wrap=plt.quiver) as mock_quiver:
            flow_legend()
            self.assertNotIn('pivot', mock_quiver.call_args.kwargs)

    def test_addition_of_plt_show_call(self):
        """Test that plt.show() is called to display the plot."""
        with patch('matplotlib.pyplot.show') as mock_show:
            flow_legend()
            mock_show.assert_called()

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