import unittest
import pandas as pd
import requests
from unittest.mock import patch, call, MagicMock
import re
import ast
import inspect

from yfinance import ingest

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


class TestIngest(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(ingest)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_encapsulate(self):
        self.assertTrue(callable(ingest))

    def test_add_type_annotations(self):
        annotations = ingest.__annotations__
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], pd.DataFrame)

    def test_import_pandas(self):
        matched_import = re.search(r'import\s+pandas', self.source)
        self.assertIsNotNone(matched_import)

    @patch('requests.get', create=True)
    def test_add_timeout(self, mock_get):
        ingest()
        for call_args in mock_get.call_args_list:
            self.assertIn('timeout', call_args.kwargs)
            self.assertEqual(call_args.kwargs['timeout'], 30)

    @patch('requests.get', create=True)
    def test_symbols(self, mock_get):
        ingest()
        params = mock_get.call_args_list[2].kwargs['params']
        symbol_str = "GOOG,TSLA,AAPL,MSFT"
        self.assertEqual(symbol_str, params['symbols'])

    @patch('requests.get')
    def test_create_dataframe(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "quoteResponse": {
                "result": [
                    {"symbol": "GOOG", "regularMarketPrice": 121.08},
                    {"symbol": "TSLA", "regularMarketPrice": 256.24},
                    {"symbol": "AAPL", "regularMarketPrice": 145.09},
                    {"symbol": "MSFT", "regularMarketPrice": 300.21},
                ]
            }
        }
        mock_get.return_value = mock_response

        df = ingest()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('metric_name', df.columns)
        self.assertIn('metric_value', df.columns)


    def test_remove_print(self):
        matched_print = re.search(r'\sprint\(', self.source)
        self.assertIsNone(matched_print)

    @patch('requests.get')
    def test_add_timestamp(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "quoteResponse": {
                "result": [
                    {"symbol": "GOOG", "regularMarketPrice": 121.08},
                    {"symbol": "TSLA", "regularMarketPrice": 256.24},
                    {"symbol": "AAPL", "regularMarketPrice": 145.09},
                    {"symbol": "MSFT", "regularMarketPrice": 300.21},
                ]
            }
        }
        mock_get.return_value = mock_response

        df = ingest()
        self.assertIn('metric_timestamp', df.columns)

    @patch('requests.get')
    def test_ingest(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "quoteResponse": {
                "result": [
                    {"symbol": "GOOG", "regularMarketPrice": 121.08},
                    {"symbol": "TSLA", "regularMarketPrice": 256.24},
                    {"symbol": "AAPL", "regularMarketPrice": 145.09},
                    {"symbol": "MSFT", "regularMarketPrice": 300.21},
                ]
            }
        }
        mock_get.return_value = mock_response

        df = ingest()
        expected_data = {
            'metric_name': ['yf_goog_price', 'yf_tsla_price', 'yf_aapl_price', 'yf_msft_price'],
            'metric_value': [121.08, 256.24, 145.09, 300.21],
        }
        expected_df = pd.DataFrame(expected_data)
        expected_df["metric_timestamp"] = pd.Timestamp.utcnow()

        pd.testing.assert_frame_equal(df.drop(columns=['metric_timestamp']),
                                      expected_df.drop(columns=['metric_timestamp']))
        self.assertAlmostEqual(df['metric_timestamp'][0].timestamp(), pd.Timestamp.utcnow().timestamp(), delta=1)


if __name__ == '__main__':
    unittest.main()
