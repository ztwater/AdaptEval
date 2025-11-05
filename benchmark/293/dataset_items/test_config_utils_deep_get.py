import unittest
from config_utils import deep_get

class TestDeepGet(unittest.TestCase):

    def setUp(self):
        # Initialize the nested dictionary for testing
        self.nested_dict = {
            'meta': {
                'status': 'OK',
                'status_code': 200,
                'details': {
                    'message': 'Success'
                }
            },
            'empty_dict': {}
        }

    def test_deep_get_with_list_keys(self):
        # Test with list of keys
        self.assertEqual(deep_get(self.nested_dict, ['meta', 'status_code']), 200)
        self.assertIsNone(deep_get(self.nested_dict, ['meta', 'non_existent_key']))

    def test_deep_get_with_string_keys(self):
        # Test with string of keys
        self.assertEqual(deep_get(self.nested_dict, 'meta.status_code'), 200)
        self.assertIsNone(deep_get(self.nested_dict, 'meta.non_existent_key'))

    def test_deep_get_with_default_value(self):
        # Test with default value
        self.assertEqual(deep_get(self.nested_dict, ['meta', 'non_existent_key'], default='Default'), 'Default')
        self.assertEqual(deep_get(self.nested_dict, 'meta.non_existent_key', default='Default'), 'Default')

    def test_deep_get_with_empty_dict(self):
        # Test with an empty dictionary
        self.assertEqual(deep_get({}, ['meta', 'status_code']), None)

    def test_deep_get_with_empty_keys(self):
        # Test with an empty list of keys
        self.assertEqual(deep_get(self.nested_dict, []), self.nested_dict)

    def test_deep_get_with_nested_empty_dict(self):
        # Test with a nested empty dictionary
        self.assertEqual(deep_get(self.nested_dict, ['empty_dict', 'non_existent_key']), None)

if __name__ == '__main__':
    unittest.main()