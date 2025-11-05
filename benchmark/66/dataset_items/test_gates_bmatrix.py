import inspect
import re
import unittest
import numpy as np
from typing import Any
from unittest.mock import patch

from gates import bmatrix
Array = Any


class TestBmatrix(unittest.TestCase):
    def test_three_dimension_array(self):
        a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        with self.assertRaises(ValueError):
            bmatrix(a)

    def test_two_dimension_array_integers(self):
        a = np.array([[1, 2], [3, 4]])
        expected_output = r"\begin{bmatrix}    1 & 2\\    3 & 4 \end{bmatrix}"
        self.assertEqual(bmatrix(a), expected_output)

    def test_two_dimension_array_floats(self):
        a = np.array([[1.1, 2.2], [3.3, 4.4]])
        expected_output = r"\begin{bmatrix}    1.1 & 2.2\\    3.3 & 4.4 \end{bmatrix}"
        # Also Check that using np.array2string would give an incorrect output: 
        # "\begin{bmatrix}    1.10e+00 & 2.20e+00\\    3.30e+00 & 4.40e+00 \end{bmatrix}"
        self.assertEqual(bmatrix(a), expected_output)

    def test_two_dimension_array_complex(self):
        a = np.array([[1+1j, 2+2j], [3+3j, 4+4j]])
        expected_output = r"\begin{bmatrix}    1.+1.j & 2.+2.j\\    3.+3.j & 4.+4.j \end{bmatrix}"
        self.assertEqual(bmatrix(a), expected_output)
        
    def test_cutoff_last_characters(self):
        a = np.array([[1, 2], [3, 4]])
        result = bmatrix(a)
        # Check that the last '\\' is correctly removed before adding \end{bmatrix}
        expected_output = r"\begin{bmatrix}    1 & 2\\    3 & 4 \end{bmatrix}"
        self.assertEqual(result, expected_output)

    def test_add_type_annotations(self):
        annotations = bmatrix.__annotations__
        expected = {
            "a": Array,
            "return": str
        }
        self.assertEqual(annotations, expected)

    @patch("numpy.array2string")
    def test_change_array_conversion(self, mock_array2string):
        a = np.array([[1, 2], [3, 4]])
        bmatrix(a)
        mock_array2string.assert_not_called()
        matched_str = re.search(r'str\(a\)', inspect.getsource(bmatrix))
        self.assertIsNotNone(matched_str)


if __name__ == '__main__':
    unittest.main()
