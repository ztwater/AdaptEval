import unittest
import inspect
import re

from ctx_collections import mapping_update_recursively


class TestMappingUpdateRecursively(unittest.TestCase):
    
    def setUp(self):
        # Initialize test data
        self.d = {
            'key1': 'value1',
            'key2': {
                'subkey1': 'subvalue1',
                'subkey2': 'subvalue2'
            },
            'key3': 'value3'
        }
        self.u = {
            'key1': 'new_value1',
            'key2': {
                'subkey1': 'new_subvalue1',
                'subkey3': 'subvalue3'
            },
            'key4': 'value4'
        }
        self.source = inspect.getsource(mapping_update_recursively)

    def test_basic_update(self):
        mapping_update_recursively(self.d, self.u)
        self.assertEqual(self.d['key1'], 'new_value1')
        self.assertEqual(self.d['key4'], 'value4')

    def test_nested_update(self):
        mapping_update_recursively(self.d, self.u)
        self.assertEqual(self.d['key2']['subkey1'], 'new_subvalue1')
        self.assertEqual(self.d['key2']['subkey3'], 'subvalue3')

    def test_existing_key_no_dict(self):
        mapping_update_recursively(self.d, {'key3': 'new_value3'})
        self.assertEqual(self.d['key3'], 'new_value3')

    def test_empty_update(self):
        mapping_update_recursively(self.d, {})
        self.assertEqual(self.d['key1'], 'value1')
        self.assertEqual(self.d['key2']['subkey1'], 'subvalue1')
        self.assertEqual(self.d['key3'], 'value3')

    def test_empty_input_dict(self):
        empty_dict = {}
        mapping_update_recursively(empty_dict, self.u)
        self.assertEqual(empty_dict, self.u)

    def test_update_function_name(self):
        mapping_update_recursively({}, self.u)

    def test_update_dict_iterator_api(self):
        matched_items = re.search(r'\.items\(\)', self.source)
        matched_iteritems = re.search(r'\.iteritems\(\)', self.source)
        self.assertIsNone(matched_iteritems)
        self.assertIsNotNone(matched_items)

    def test_update_package_namesapce(self):
        matched_package = re.search(r'collections\.Mapping', self.source)
        self.assertIsNone(matched_package)

if __name__ == '__main__':
    unittest.main()
