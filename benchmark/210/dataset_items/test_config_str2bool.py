import unittest
import argparse
from typing import Union

from config import str2bool
    

class TestStr2bool(unittest.TestCase):

    def test_boolean_values(self):
        self.assertTrue(str2bool(True))
        self.assertFalse(str2bool(False))

    def test_string_true_variations(self):
        self.assertTrue(str2bool("true"))
        self.assertTrue(str2bool("True"))
        self.assertTrue(str2bool("t"))
        self.assertTrue(str2bool("yes"))
        self.assertTrue(str2bool("y"))
        self.assertTrue(str2bool("1"))

    def test_string_false_variations(self):
        self.assertFalse(str2bool("false"))
        self.assertFalse(str2bool("False"))
        self.assertFalse(str2bool("f"))
        self.assertFalse(str2bool("no"))
        self.assertFalse(str2bool("n"))
        self.assertFalse(str2bool("0"))

    def test_invalid_value(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            str2bool("invalid")

    def test_add_annotations(self):
        annotations = str2bool.__annotations__
        expected = {'v': 'Union[str, bool]', 'return': 'bool'}
        self.assertEqual(annotations, expected)

    def test_logic_expansion(self):
        self.assertTrue(str2bool("True"))
        self.assertFalse(str2bool("False"))


if __name__ == "__main__":
    unittest.main()
