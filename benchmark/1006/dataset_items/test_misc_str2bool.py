import unittest
import argparse

from misc import str2bool


class TestStr2bool(unittest.TestCase):

    def test_true_values(self):
        """Tests if various True representations are converted correctly."""
        self.assertTrue(str2bool("yes"))
        self.assertTrue(str2bool("true"))
        self.assertTrue(str2bool("t"))
        self.assertTrue(str2bool("y"))
        self.assertTrue(str2bool("1"))
        self.assertTrue(str2bool("True"))  # Test case for uppercase 'True'

    def test_false_values(self):
        """Tests if various False representations are converted correctly."""
        self.assertFalse(str2bool("no"))
        self.assertFalse(str2bool("false"))
        self.assertFalse(str2bool("f"))
        self.assertFalse(str2bool("n"))
        self.assertFalse(str2bool("0"))
        self.assertFalse(str2bool("False"))  # Test case for uppercase 'False'

    def test_invalid_value(self):
        """Tests if an invalid value raises an ArgumentTypeError."""
        self.assertRaises(argparse.ArgumentTypeError, str2bool, "invalid")

    def test_delete_if_condition(self):
        self.assertRaises(AttributeError, str2bool, True)


if __name__ == "__main__":
    unittest.main()
