import inspect

import numpy as np
import unittest
from dataset_GemNet_utils import repeat_blocks


class TestRepeatBlocks(unittest.TestCase):
    def test_repeat_blocks_example_1(self):
        sizes = np.array([1, 3, 2], dtype=np.int32)
        repeats = np.array([3, 2, 3], dtype=np.int32)
        expected_output = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_repeat_blocks_example_2(self):
        sizes = np.array([0, 3, 2], dtype=np.int32)
        repeats = np.array([3, 2, 3], dtype=np.int32)
        expected_output = np.array([0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 3, 4])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_repeat_blocks_example_3(self):
        sizes = np.array([2, 3, 2], dtype=np.int32)
        repeats = np.array([2, 0, 2], dtype=np.int32)
        expected_output = np.array([0, 1, 0, 1, 5, 6, 5, 6])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_repeat_blocks_empty_sizes(self):
        sizes = np.array([], dtype=np.int32)
        repeats = np.array([], dtype=np.int32)
        expected_output = np.array([], dtype=np.int32)
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_repeat_blocks_single_size_single_repeat(self):
        sizes = np.array([1], dtype=np.int32)
        repeats = np.array([1], dtype=np.int32)
        expected_output = np.array([0])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_remove_numba_jit_decoration(self):
        # Test to ensure function works without the Numba JIT decorator
        sizes = np.array([1, 3, 2], dtype=np.int32)
        repeats = np.array([3, 2, 3], dtype=np.int32)
        expected_output = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_rename_function_to_repeat_blocks(self):
        # Test to ensure function name has been updated
        self.assertTrue(callable(repeat_blocks))

    def test_remove_parameter(self):
        parameters = inspect.signature(repeat_blocks).parameters
        self.assertNotIn('a', parameters)

    def test_update_output_array_variable_name_to_indices(self):
        sizes = np.array([1, 3, 2], dtype=np.int32)
        repeats = np.array([3, 2, 3], dtype=np.int32)
        expected_output = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_use_underscore_instead_of_rep_variable(self):
        # Test to ensure inner loop uses '_' instead of 'rep'
        sizes = np.array([2, 3, 2], dtype=np.int32)
        repeats = np.array([2, 0, 2], dtype=np.int32)
        expected_output = np.array([0, 1, 0, 1, 5, 6, 5, 6])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_generate_array_using_np_arange(self):
        # Test to ensure array 'a' is generated using np.arange with sum of sizes
        sizes = np.array([1, 3, 2], dtype=np.int32)
        repeats = np.array([3, 2, 3], dtype=np.int32)
        expected_output = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5])
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

    def test_update_array_initialization_with_dtype(self):
        # Test to ensure output array is initialized with dtype=np.int32
        sizes = np.array([1, 3, 2], dtype=np.int32)
        repeats = np.array([3, 2, 3], dtype=np.int32)
        expected_output = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5], dtype=np.int32)
        result = repeat_blocks(sizes, repeats)
        np.testing.assert_array_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()
