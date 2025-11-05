import unittest
import argparse

from propagation_utils import str2bool


class TestStr2bool(unittest.TestCase):

    def test_true_values(self):
        """Tests if various True representations are converted correctly."""
        self.assertTrue(str2bool("yes"))
        self.assertTrue(str2bool("true"))
        self.assertTrue(str2bool("t"))
        self.assertTrue(str2bool("y"))
        self.assertTrue(str2bool("1"))

    def test_false_values(self):
        """Tests if various False representations are converted correctly."""
        self.assertFalse(str2bool("no"))
        self.assertFalse(str2bool("false"))
        self.assertFalse(str2bool("f"))
        self.assertFalse(str2bool("n"))
        self.assertFalse(str2bool("0"))


    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            str2bool("invalid")


if __name__ == "__main__":
    unittest.main()
