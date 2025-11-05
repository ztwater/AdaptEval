import unittest
import numpy as np
import inspect

from base import get_closest


class TestGetClosest(unittest.TestCase):
    def test_basic_functionality(self):
        sorted_array = np.array([1, 3, 5, 7, 9])
        values = np.array([2, 4, 6, 8])
        expected_result = np.array([3, 5, 7, 9])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)
    
    def test_closest_to_start_and_end(self):
        sorted_array = np.array([10, 20, 30, 40, 50])
        values = np.array([5, 55])
        expected_result = np.array([10, 50])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)
    
    def test_values_exact_match(self):
        sorted_array = np.array([0, 2, 4, 6, 8, 10])
        values = np.array([2, 6, 8])
        expected_result = np.array([2, 6, 8])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)
    
    def test_negative_numbers(self):
        sorted_array = np.array([-10, -5, 0, 5, 10])
        values = np.array([-8, -3, 2, 7])
        expected_result = np.array([-10, -5, 0, 5])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)
    
    def test_empty_arrays(self):
        sorted_array = np.array([])
        values = np.array([])
        expected_result = np.array([])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)
    
    def test_single_element_arrays(self):
        sorted_array = np.array([10])
        values = np.array([10])
        expected_result = np.array([10])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)

    def test_sorted_array_type(self):
        sorted_array = [1, 2, 3]
        values = np.array([2])
        with self.assertRaises(TypeError):
            get_closest(sorted_array, values)
   
    def test_value_type(self):
        sorted_array = np.array([1, 2, 3])
        values = [2]
        expected_result = np.array([2])
        np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)

    def test_add_type_annotations(self):
        annotations = get_closest.__annotations__
        expected = {
            'sorted_array': 'NDArray',
            'values': 'NDArray',
            'return': 'NDArray'
        }
        self.assertEqual(annotations, expected)

    def test_remove_array_conversion(self):
        # sorted array without conversion
        sorted_array = [1, 3, 5, 7, 9]
        values = np.array([2, 4, 6, 8])
        expected_result = np.array([3, 5, 7, 9])
        with self.assertRaises(TypeError):
            np.testing.assert_array_equal(get_closest(sorted_array, values), expected_result)

    def test_rename_parameter(self):
        parameters = inspect.signature(get_closest).parameters
        self.assertIn('sorted_array', parameters)
        self.assertNotIn('array', parameters)


if __name__ == '__main__':
    unittest.main()
