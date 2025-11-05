import unittest
import types
import copy
import functools

from type import copy_func


class TestCopyFunc(unittest.TestCase):
    def setUp(self):
        def original_function(x):
            return x + 1
        
        self.original_function = original_function
        self.copied_function = copy_func(original_function)

    def test_copy_func_returns_correct_result(self):
        self.assertEqual(self.copied_function(1), 2)

    def test_copy_func_preserves_name(self):
        self.assertEqual(self.copied_function.__name__, self.original_function.__name__)

    def test_copy_func_copies_globals(self):
        def function_with_global():
            return GLOBAL_VAR
        global GLOBAL_VAR
        GLOBAL_VAR = 42
        copied_function_with_global = copy_func(function_with_global)
        GLOBAL_VAR = 24
        self.assertEqual(copied_function_with_global(), 42)

    def test_add_type_annotations(self):
        annotations = copy_func.__annotations__
        self.assertIn('f', annotations)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['f'], 'T')
        self.assertEqual(annotations['return'], 'T')

if __name__ == '__main__':
    unittest.main()
