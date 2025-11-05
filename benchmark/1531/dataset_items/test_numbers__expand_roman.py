import unittest
import re
import inspect
from unittest.mock import MagicMock

from ctx_numbers import _expand_roman
 

class TestExpandRoman(unittest.TestCase):
    def test_sample(self):
        pattern = re.compile(r'[IVXLCDM]+')
        match = pattern.match('XIV')
        self.assertEqual(_expand_roman(match), '14')

    def test_rename_function(self):
        import numbers
        self.assertTrue(callable(_expand_roman))
        self.assertNotIn('from_roman', numbers.__dict__)

    def test_update_parameter(self):
        parameters = inspect.signature(_expand_roman).parameters
        self.assertIn('m', parameters)

    def test_implicit_parameter_type_change(self):
        with self.assertRaises(AttributeError):
            _expand_roman("XIV")

    def test_number_retrieval(self):
        mock_match = MagicMock()
        mock_group = MagicMock()
        mock_match.group = mock_group
        _expand_roman(mock_match)
        mock_group.assert_called_with(0)

    def test_return_type(self):
        pattern = re.compile(r'[IVXLCDM]+')
        match = pattern.match('MCMXCIV')
        self.assertIsInstance(_expand_roman(match), str)

    def test_single_roman_numeral(self):
        pattern = re.compile(r'[IVXLCDM]+')
        match = pattern.match('V')
        self.assertEqual(_expand_roman(match), '5')

    def test_complex_roman_numeral(self):
        pattern = re.compile(r'[IVXLCDM]+')
        match = pattern.match('MMXVIII')
        self.assertEqual(_expand_roman(match), '2018')

if __name__ == "__main__":
    unittest.main()