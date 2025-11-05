import unittest
import numpy as np
import scipy.stats

from statistics_utility import mean_confidence_interval

class TestMeanConfidenceInterval(unittest.TestCase):

    def test_basic_functionality(self):
        data = [1, 2, 3, 4, 5]
        confidence = 0.95
        expected_margin_of_error = scipy.stats.sem(data) * scipy.stats.t.ppf((1 + confidence) / 2., len(data) - 1)
        self.assertAlmostEqual(mean_confidence_interval(data, confidence), expected_margin_of_error)

    def test_confidence_level(self):
        data = [1, 2, 3, 4, 5]
        confidence = 0.99
        expected_margin_of_error = scipy.stats.sem(data) * scipy.stats.t.ppf((1 + confidence) / 2., len(data) - 1)
        self.assertAlmostEqual(mean_confidence_interval(data, confidence), expected_margin_of_error)

    def test_non_numeric_data(self):
        data = ['a', 'b', 'c']
        confidence = 0.95
        with self.assertRaises(TypeError):
            mean_confidence_interval(data, confidence)

    def test_change_return_value(self):
        data = [1, 2, 3, 4, 5]
        confidence = 0.95
        result = mean_confidence_interval(data, confidence)
        self.assertIsInstance(result, np.float_)
        self.assertNotIsInstance(result, tuple)

if __name__ == '__main__':
    unittest.main()
