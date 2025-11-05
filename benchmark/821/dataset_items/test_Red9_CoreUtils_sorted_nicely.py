import inspect
import unittest
import re
from Red9_CoreUtils import sorted_nicely

class TestSortedNicely(unittest.TestCase):
    def test_sort_with_numbers(self):
        self.assertEqual(sorted_nicely(['42', '3', '1']), ['1', '3', '42'])

    def test_sort_with_alphanumeric(self):
        self.assertEqual(sorted_nicely(['item42', 'item3', 'item1']), ['item1', 'item3', 'item42'])

    def test_sort_with_mixed(self):
        self.assertEqual(sorted_nicely(['item42', '3', 'item1', '1']), ['1', '3' , 'item1' , 'item42'])

    def test_sort_with_no_numbers(self):
        self.assertEqual(sorted_nicely(['apple', 'banana', 'cherry']), ['apple', 'banana', 'cherry'])

    def test_sort_with_negative_numbers(self):
        self.assertEqual(sorted_nicely(['-42', '-3', '-1']), ['-1', '-3', '-42'])

    def test_sort_with_float_numbers(self):
        self.assertEqual(sorted_nicely(['3.14', '1.59', '2.65']), ['1.59', '2.65', '3.14'])

    def test_sort_with_empty_strings(self):
        self.assertEqual(sorted_nicely(['', '2', '1']), ['', '1', '2'])

    def test_update_parameter_name(self):
        parameters = inspect.signature(sorted_nicely).parameters
        self.assertIn('items', parameters)
        self.assertNotIn('l', parameters)


if __name__ == '__main__':
    unittest.main()