import inspect
import re
import unittest
from typing import Iterator, get_type_hints

from db_utils import gen_dict_extract

class TestGenDictExtract(unittest.TestCase):
    
    def test_single_level_dict(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        expected = [1]
        result = list(gen_dict_extract('a', data))
        self.assertEqual(result, expected)

    def test_nested_dict(self):
        data = {'a': 1, 'b': {'a': 2, 'c': 3}, 'd': {'e': {'a': 4}}}
        expected = [1, 2, 4]
        result = list(gen_dict_extract('a', data))
        self.assertEqual(result, expected)
        
    def test_list_of_dicts(self):
        data = {'a': [{'b': 1}, {'a': 2}], 'c': 3}
        expected = [[{'b': 1}, {'a': 2}], 2]
        result = list(gen_dict_extract('a', data))
        self.assertEqual(result, expected)
        
    def test_complex_structure(self):
        data = {
            'a': 1,
            'b': [{'a': 2, 'b': {'a': 3}}, {'c': {'a': 4}}],
            'd': {'e': [{'a': 5}]}
        }
        expected = [1, 2, 3, 4, 5]
        result = list(gen_dict_extract('a', data))
        self.assertEqual(result, expected)
        
    def test_key_not_present(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        expected = []
        result = list(gen_dict_extract('z', data))
        self.assertEqual(result, expected)

    def test_non_dict_input(self):
        data = ['a', 'b', 'c']
        expected = []
        result = list(gen_dict_extract('a', data))
        self.assertEqual(result, expected)
        
    def test_annotations(self):
        expected_annotations = {'key_': str, 'dict_': dict, 'return': Iterator}
        actual_annotations = get_type_hints(gen_dict_extract)
        self.assertEqual(actual_annotations, expected_annotations)
        
    def test_parameter_renaming(self):
        parameters = list(inspect.signature(gen_dict_extract).parameters.keys())
        self.assertIn('key_', parameters)
        self.assertIn('dict_', parameters)
        self.assertEqual('key_', parameters[0])
        self.assertEqual('dict_', parameters[1])
        with self.assertRaises(TypeError):
            # This should raise a TypeError because the function no longer accepts 'var' and 'keys' as parameters
            gen_dict_extract(var='a', keys={'a': 1, 'b': {'a': 2, 'c': 3}, 'd': {'e': {'a': 4}}})

    def test_for_removing(self):
        source = inspect.getsource(gen_dict_extract)
        matched_for = re.search(r'\bfor\s+[A-Za-z_][A-Za-z0-9_]*\s+in\s+keys:', source)
        self.assertIsNone(matched_for)

if __name__ == '__main__':
    unittest.main()
