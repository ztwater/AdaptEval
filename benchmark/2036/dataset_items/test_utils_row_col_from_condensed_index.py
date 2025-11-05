import unittest
import math

# Assuming the function is defined in the same file or imported from another module
from ctx_utils import row_col_from_condensed_index

class TestRowColFromCondensedIndex(unittest.TestCase):
    def test_basic_functionality(self):
        # Test with a simple case where d = 3 (4 observations)
        self.assertEqual(row_col_from_condensed_index(3, 0), (0, 1))
        self.assertEqual(row_col_from_condensed_index(3, 1), (0, 2))
        self.assertEqual(row_col_from_condensed_index(3, 3), (2, 3))

    def test_edge_cases(self):
        # Test with edge cases for the condensed index
        self.assertEqual(row_col_from_condensed_index(2, 0), (0, 1))
        self.assertEqual(row_col_from_condensed_index(1, 0), (0, 1))  # Only one element, so index 0 is itself

    def test_large_index(self):
        # Test with a large index to ensure the function handles large numbers correctly
        d = 10  # 11 observations
        index = 45  # This is the last index in the condensed matrix for d=10
        expected_i = 9
        expected_j = 10
        self.assertEqual(row_col_from_condensed_index(d, index), (expected_i, expected_j))

    def test_int_adaptation(self):
        results = row_col_from_condensed_index(10, 10.5)
        self.assertEqual(results, (1, 3))
        self.assertIsInstance(results[0], int)
        self.assertIsInstance(results[1], int)


if __name__ == '__main__':
    unittest.main()