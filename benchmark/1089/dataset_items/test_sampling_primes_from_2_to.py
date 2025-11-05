import unittest
from unittest.mock import patch
import numpy as np
import inspect

import sampling
from sampling import primes_from_2_to


def list_primes(limit):
    primes = set(range(2, limit + 1))
    for i in range(2, limit + 1):
        if i in primes:
            primes.difference_update(set(list(range(i, limit + 1, i))[1:]))
    return np.array(sorted(primes))


class TestPrimesFrom2To(unittest.TestCase):
    def assertNpArrEquals(self, arr1, arr2):
        self.assertFalse(np.all(arr1 - np.array(arr2)))

    def test_small_primes(self):
        self.assertNpArrEquals(primes_from_2_to(10), [2, 3, 5, 7])

    def test_medium_primes(self):
        self.assertNpArrEquals(primes_from_2_to(100), list_primes(100))

    def test_large_primes(self):
        self.assertNpArrEquals(primes_from_2_to(1000), list_primes(1000))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            primes_from_2_to(3.14)

    def test_n_equals_2(self):
        self.assertNpArrEquals(primes_from_2_to(2), [2])

    def test_func_name_change(self):
        self.assertNotEqual(primes_from_2_to.__name__, 'primesfrom2to')

    def test_numpy_abbr_change(self):
        self.assertIn('np', sampling.__dict__)
        self.assertNotIn('numpy', sampling.__dict__)

    @patch('numpy.ones')
    def test_np_bool_refactor(self, mock_ones):
        primes_from_2_to(10)
        _, kwargs = mock_ones.call_args
        self.assertIn('dtype', kwargs)
        self.assertEqual(kwargs['dtype'], np.bool_)
        self.assertNotEqual(kwargs['dtype'], bool)


if __name__ == '__main__':
    unittest.main()
