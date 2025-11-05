import inspect, re, ast
import unittest
from unittest.mock import MagicMock, patch, call
import pandas as pd
from ocr import unnest

class TestUnnest(unittest.TestCase):
    def setUp(self):
        # Set up a DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2],
            'B': [[1, 2], [3, 4]],
            'C': [[1, 2], [3, 4]]
        })
        self.explode_columns = ['B', 'C']
        self.axis = 1  # Unnest along columns

        source = inspect.getsource(unnest)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_unnest_along_columns(self):
        # Test unnesting along columns
        result = unnest(self.df, self.explode_columns, self.axis)
        self.assertEqual(result['A'].tolist(), [1, 1, 2, 2])
        self.assertEqual(result['B'].tolist(), [1, 2, 3, 4])
        self.assertEqual(result['C'].tolist(), [1, 2, 3, 4])

    def test_unnest_along_rows(self):
        result = unnest(self.df, self.explode_columns, 0)
        self.assertEqual(result['A'].tolist(), [1, 2])
        self.assertEqual(result['B0'].tolist(), [1, 3])
        self.assertEqual(result['B1'].tolist(), [2, 4])
        self.assertEqual(result['C0'].tolist(), [1, 3])
        self.assertEqual(result['C1'].tolist(), [2, 4])

    def test_unnest_with_suffixes(self):
        # Test unnesting with suffixes
        suffixes = ['_suffix1', '_suffix2']
        result = unnest(self.df, self.explode_columns, 0, suffixes)
        expected_columns = ['B_suffix1', 'B_suffix2', 'C_suffix1', 'C_suffix2', 'A']
        self.assertEqual(result.columns.tolist(), expected_columns)

    def test_unnest_with_empty_explode_list(self):
        # Test unnesting with an empty list of columns to explode
        with self.assertRaises(ValueError):
            unnest(self.df, [], self.axis)

    def test_unnest_with_invalid_axis(self):
        # Test unnesting with an invalid axis value
        result = unnest(self.df, self.explode_columns, 'invalid_axis')
        result_0 = unnest(self.df, self.explode_columns, 0)
        pd.testing.assert_frame_equal(result, result_0)

    def test_rename_function(self):
        from ocr import unnest
        self.assertTrue(callable(unnest))

    def test_add_type_annotations(self):
        annotations = unnest.__annotations__
        self.assertIn('df', annotations)
        self.assertEqual(annotations['df'], pd.DataFrame)
        self.assertIn('explode', annotations)
        self.assertEqual(annotations['explode'], list)
        self.assertIn('axis', annotations)
        self.assertEqual(annotations['axis'], int)
        self.assertIn('suffixes', annotations)
        self.assertEqual(annotations['suffixes'], list)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], pd.DataFrame)

    def test_add_default_parameter(self):
        parameters = inspect.signature(unnest).parameters
        self.assertIn('suffixes', parameters)
        self.assertEqual(parameters['suffixes'].default, None)

    def test_specify_parameter_name(self):
        matched_axis = re.search(r'df\.drop\(.*,\s*axis=1\s*\)', self.source)
        self.assertIsNotNone(matched_axis)

    @patch('pandas.concat')
    def test_add_columns_parameter(self, mock_concat):
        mock_new = MagicMock()
        with patch('pandas.DataFrame', new=mock_new) as mock_df:
            suffixes = ['_suffix1', '_suffix2']
            unnest(self.df, self.explode_columns, 0, suffixes)
            self.assertIn('columns', mock_df.call_args.kwargs)
            self.assertEqual(suffixes,  mock_df.call_args.kwargs['columns'])


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
