import unittest
from unittest.mock import patch
import numpy as np

from normalization import empirical_cdf
 
class TestEmpiricalCdf(unittest.TestCase):
    def test_sample(self):
        sample = np.array([1, 2, 2, 3, 3, 3])
        quantiles, cumprob = empirical_cdf(sample)
        expected_quantiles = np.array([1, 2, 3])
        expected_cumprob = np.array([1/6, 3/6, 6/6])
        np.testing.assert_array_equal(quantiles, expected_quantiles)
        np.testing.assert_array_equal(cumprob, expected_cumprob)
        
    def test_function_rename(self):
        import normalization
        self.assertTrue(callable(empirical_cdf))
        self.assertFalse('ecdf' in normalization.__dict__)

    @patch('numpy.atleast_1d', return_value=np.array([]))
    def test_sample_conversion(self, mock_atleast):
        sample = [1, 2, 2, 3, 3, 3]
        with self.assertRaises(AttributeError):
            quantiles, cumprob = empirical_cdf(sample)
        mock_atleast.assert_not_called()

    def test_normal_sample(self):
        sample = np.array([1, 2, 2, 3, 3, 3])
        quantiles, cumprob = empirical_cdf(sample)
        expected_quantiles = np.array([1, 2, 3])
        expected_cumprob = np.array([1/6, 3/6, 6/6])
        np.testing.assert_array_equal(quantiles, expected_quantiles)
        np.testing.assert_array_equal(cumprob, expected_cumprob)

    def test_empty_sample(self):
        sample = np.array([])
        quantiles, cumprob = empirical_cdf(sample)
        expected_quantiles = np.array([])
        expected_cumprob = np.array([])
        np.testing.assert_array_equal(quantiles, expected_quantiles)
        np.testing.assert_array_equal(cumprob, expected_cumprob)

    def test_single_element_sample(self):
        sample = np.array([5])
        quantiles, cumprob = empirical_cdf(sample)
        expected_quantiles = np.array([5])
        expected_cumprob = np.array([1.0])
        np.testing.assert_array_equal(quantiles, expected_quantiles)
        np.testing.assert_array_equal(cumprob, expected_cumprob)

if __name__ == "__main__":
    unittest.main()
