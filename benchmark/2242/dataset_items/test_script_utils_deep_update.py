import unittest
from unittest.mock import patch

from script_utils import deep_update

class TestDeepUpdate(unittest.TestCase):

    def test_update_method_name(self):
        import script_utils
        self.assertTrue(callable(deep_update))
        self.assertNotIn('update', script_utils.__dict__)

    @patch('builtins.__import__', wraps=__import__)
    def test_insert_import(self, mock_import):
        original_dict = {'key1': 'value1', 'key2': 'value2'}
        update_dict = {'key1': 'new_value1'}
        deep_update(original_dict, update_dict)
        self.assertEqual('collections', mock_import.call_args.args[0])

    def test_update_top_level_key(self):
        original_dict = {'key1': 'value1', 'key2': 'value2'}
        update_dict = {'key1': 'new_value1'}
        expected_result = {'key1': 'new_value1', 'key2': 'value2'}
        self.assertEqual(deep_update(original_dict, update_dict), expected_result)

    def test_update_nested_key(self):
        original_dict = {'level1': {'key1': 'value1'}}
        update_dict = {'level1': {'key1': 'new_value1'}}
        expected_result = {'level1': {'key1': 'new_value1'}}
        self.assertEqual(deep_update(original_dict, update_dict), expected_result)

    def test_update_nested_with_new_key(self):
        original_dict = {'level1': {'key1': 'value1'}}
        update_dict = {'level1': {'new_key': 'new_value'}}
        expected_result = {'level1': {'key1': 'value1', 'new_key': 'new_value'}}
        self.assertEqual(deep_update(original_dict, update_dict), expected_result)

    def test_overwrite_non_mapping_value(self):
        original_dict = {'key1': 'value1', 'key2': {'subkey1': 'subvalue1'}}
        update_dict = {'key2': 'completely_new_value'}
        expected_result = {'key1': 'value1', 'key2': 'completely_new_value'}
        self.assertEqual(deep_update(original_dict, update_dict), expected_result)

    def test_deeply_nested_update(self):
        original_dict = {'level1': {'level2': {'key1': 'value1'}}}
        update_dict = {'level1': {'level2': {'key1': 'new_value1', 'new_key': 'new_value'}}}
        expected_result = {'level1': {'level2': {'key1': 'new_value1', 'new_key': 'new_value'}}}
        self.assertEqual(deep_update(original_dict, update_dict), expected_result)

    def test_mixed_types_update(self):
        original_dict = {'list_key': [1, 2, 3], 'dict_key': {'key1': 'value1'}}
        update_dict = {'list_key': 'overwritten', 'dict_key': {'key1': 'new_value1'}}
        expected_result = {'list_key': 'overwritten', 'dict_key': {'key1': 'new_value1'}}
        self.assertEqual(deep_update(original_dict, update_dict), expected_result)

if __name__ == "__main__":
    unittest.main()
