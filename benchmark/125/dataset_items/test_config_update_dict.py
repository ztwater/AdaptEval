import unittest
from unittest.mock import patch, MagicMock
from collections.abc import Mapping
from typing import Dict
import inspect
import re

from config import update_dict

class TestUpdateDict(unittest.TestCase):

    def test_simple_update(self):
        d = {'a': 1, 'b': 2}
        u = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(update_dict(d, u), expected)

    def test_nested_update(self):
        d = {'a': {'x': 1}, 'b': 2}
        u = {'a': {'y': 2}, 'b': 3, 'c': 4}
        expected = {'a': {'x': 1, 'y': 2}, 'b': 3, 'c': 4}
        self.assertEqual(update_dict(d, u), expected)

    def test_no_update_needed(self):
        d = {'a': 1, 'b': 2}
        u = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(update_dict(d, u), expected)

    def test_empty_dict(self):
        d = {}
        u = {'a': 1, 'b': {'x': 10}}
        expected = {'a': 1, 'b': {'x': 10}}
        self.assertEqual(update_dict(d, u), expected)

    def test_type_annotations(self):
        self.assertEqual(update_dict.__annotations__, {'d': Dict, 'u': Mapping, 'return': Dict})

    def test_update_function_name(self):
        d = {'a': 1, 'b': 2}
        u = {'b': 3, 'c': 4}
        update_dict(d, u)

    def test_change_api_name(self):
        source = inspect.getsource(update_dict)
        matched_api = re.search(r'collections\.abc\.Mapping', source)
        self.assertIsNone(matched_api)


if __name__ == '__main__':
    unittest.main()
