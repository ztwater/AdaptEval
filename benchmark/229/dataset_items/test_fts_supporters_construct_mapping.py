import unittest
import yaml
from typing import Dict
import inspect
import re

from fts_supporters import UniqueKeyLoader


class TestConstructMapping(unittest.TestCase):

    def setUp(self):
        self.loader_class = UniqueKeyLoader

    def test_no_duplicate_keys(self):
        yaml_str = """
        key1: value1
        key2: value2
        """
        try:
            yaml.load(yaml_str, Loader=self.loader_class)
        except ValueError:
            self.fail("UniqueKeyLoader raised ValueError unexpectedly!")

    def test_with_duplicate_keys(self):
        yaml_str = """
        key1: value1
        key1: value2
        """
        with self.assertRaises(ValueError) as context:
            yaml.load(yaml_str, Loader=self.loader_class)
        self.assertEqual(str(context.exception), 'key1')

    def test_type_annotations(self):
        method = self.loader_class.construct_mapping
        self.assertEqual(method.__annotations__, {
            'node': yaml.MappingNode,
            'deep': bool,
            'return': Dict
        })

    def test_refactoring(self):
        source = inspect.getsource(self.loader_class.construct_mapping)
        matched_loop_var = re.search(r'for\s*[A-Za-z_]\w*,\s*_\s*in\s*node\.value:',
                                     source)
        self.assertIsNotNone(matched_loop_var)


if __name__ == '__main__':
    unittest.main()
