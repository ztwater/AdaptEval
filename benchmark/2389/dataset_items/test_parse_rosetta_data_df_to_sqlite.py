import unittest
import pandas as pd
import pandas
import sqlite3
from tqdm import tqdm
from parse_rosetta_data import df_to_sqlite
from pandas.io.sql import SQLiteDatabase, SQLiteTable
import inspect
from unittest.mock import patch, MagicMock, call


class TestDfToSqlite(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['A', 'B', 'C']
        })
        self.db_file_name = ':memory:'  # Use in-memory database for testing
        self.table_name = 'test_table'
        self.chunk_size = 5

    def test_update_chunk_size_default_value(self):
        # 检查默认的chunk_size是否为1000000
        annotations = df_to_sqlite.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('chunk_size', annotations)
        self.assertEqual(annotations['chunk_size'], int)

        parameters = inspect.signature(df_to_sqlite).parameters
        self.assertTrue(parameters["chunk_size"].default, 1000000)

    @patch('parse_rosetta_data.SQLiteTable', wraps=SQLiteTable)
    def test_set_index_to_false(self, sqltable_mock):
        df_to_sqlite(self.df, self.db_file_name, self.table_name)
        self.assertEqual(sqltable_mock.call_args.kwargs['index'], False)

    @patch('parse_rosetta_data.SQLiteTable', wraps=SQLiteTable)
    def test_change_if_exists_parameter(self, sqltable_mock):
        df_to_sqlite(self.df, self.db_file_name, self.table_name)
        self.assertEqual(sqltable_mock.call_args.kwargs['if_exists'], 'append')

    def test_update_index_parameter_in_itertuples(self):
        class SingleItemIterator:
            def __next__(self):
                raise StopIteration

        mock_df = MagicMock()
        mock_df.itertuples = MagicMock(return_value=SingleItemIterator())
        mock_con = MagicMock()
        with patch('sqlite3.connect', return_value=mock_con):
            with patch('parse_rosetta_data.SQLiteTable'):
                df_to_sqlite(mock_df, self.db_file_name, self.table_name)
                self.assertEqual(mock_df.itertuples.call_args.kwargs['index'], False)

    @patch('parse_rosetta_data.tqdm',wraps=tqdm)
    @patch('sqlite3.connect')
    def test_df_to_sqlite_inserts_data(self, mock_connect, mock_tqdm):
        # Mock the connection and cursor
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        # Call the function
        df_to_sqlite(self.df, self.db_file_name, self.table_name, self.chunk_size)

        # Check if the table was created
        mock_conn.execute.assert_has_calls([call('begin'), 
                                            call('INSERT INTO "test_table" ("col1","col2") VALUES (?,?)', (1, 'A')),
                                            call('INSERT INTO "test_table" ("col1","col2") VALUES (?,?)', (2, 'B')),
                                            call('INSERT INTO "test_table" ("col1","col2") VALUES (?,?)', (3, 'C')),
                                            call('commit')
                                            ])
        mock_tqdm.assert_called()
        

    def tearDown(self):
        # Close the connection to the in-memory SQLite database
        con = sqlite3.connect(self.db_file_name)
        con.close()
        
if __name__ == '__main__':
    unittest.main()
