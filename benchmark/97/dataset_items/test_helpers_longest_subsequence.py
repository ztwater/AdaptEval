import unittest
from unittest.mock import patch, MagicMock
import inspect
import re

from helpers import longest_subsequence

class TestLongestSubsequence(unittest.TestCase):

    def test_in_original_repo(self):
        dates = [
            ("2015-02-03", "name1"),
            ("2015-02-04", "nameg"),
            ("2015-02-04", "name5"),
            ("2015-02-05", "nameh"),
            ("1929-03-12", "name4"),
            ("2023-07-01", "name7"),
            ("2015-02-07", "name0"),
            ("2015-02-08", "nameh"),
            ("2015-02-15", "namex"),
            ("2015-02-09", "namew"),
            ("1980-12-23", "name2"),
            ("2015-02-12", "namen"),
            ("2015-02-13", "named"),
        ]

        self.assertEqual(longest_subsequence(dates, "weak"), [
            ("2015-02-03", "name1"),
            ("2015-02-04", "name5"),
            ("2015-02-05", "nameh"),
            ("2015-02-07", "name0"),
            ("2015-02-08", "nameh"),
            ("2015-02-09", "namew"),
            ("2015-02-12", "namen"),
            ("2015-02-13", "named"),
        ])

        from operator import itemgetter

        self.assertEqual(longest_subsequence(dates, "weak", key=itemgetter(0)), [
            ("2015-02-03", "name1"),
            ("2015-02-04", "nameg"),
            ("2015-02-04", "name5"),
            ("2015-02-05", "nameh"),
            ("2015-02-07", "name0"),
            ("2015-02-08", "nameh"),
            ("2015-02-09", "namew"),
            ("2015-02-12", "namen"),
            ("2015-02-13", "named"),
        ])

        indices = set(longest_subsequence(dates, key=itemgetter(0), index=True))
        self.assertEqual([e for i, e in enumerate(dates) if i not in indices], [
            ("2015-02-04", "nameg"),
            ("1929-03-12", "name4"),
            ("2023-07-01", "name7"),
            ("2015-02-15", "namex"),
            ("1980-12-23", "name2"),
        ])
        

    def test_decreasing_sequence(self):
        seq = [80, 60, 51, 50, 21, 33, 9, 22, 10]
        result = longest_subsequence(seq, order='decreasing')
        self.assertEqual(result, [80, 60, 51, 50, 33, 22, 10])

    def test_strictly_increasing(self):
        seq = [3, 10, 2, 1, 20]
        result = longest_subsequence(seq, mode='strictly')
        self.assertEqual(result, [3, 10, 20])

    def test_weakly_increasing(self):
        seq = [3, 3, 3, 3, 3, 3]
        result = longest_subsequence(seq, mode='weakly')
        self.assertEqual(result, [3, 3, 3, 3, 3, 3])

    def test_with_key_function(self):
        seq = ['apple', 'banana', 'apricot', 'cherry']
        result = longest_subsequence(seq, key=len)
        self.assertEqual(result, ['apple', 'banana', 'apricot'])

    def test_with_index_true(self):
        seq = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        result = longest_subsequence(seq, index=True)
        self.assertEqual(result, [0, 1, 3, 6, 7, 8])

    def test_empty_sequence(self):
        seq = []
        result = longest_subsequence(seq)
        self.assertEqual(result, [])

    def test_invalid_sequence(self):
        seq = [1, 'a', 2]
        with self.assertRaises(TypeError):
            longest_subsequence(seq)

    def test_positional_args_with_index(self):
        # Test to ensure TypeError is raised when index is provided as a positional argument
        with self.assertRaises(TypeError):
            longest_subsequence([1, 2, 3], "strictly", "increasing", None, True)

    def test_handle_exception(self):
        source = inspect.getsource(longest_subsequence)
        matched_exception = re.search(r'except\s+Exception', source)
        self.assertIsNotNone(matched_exception)

if __name__ == '__main__':
    unittest.main()
