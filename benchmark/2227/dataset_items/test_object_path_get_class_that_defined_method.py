import unittest
from unittest.mock import patch, MagicMock

from object_path import get_class_that_defined_method

class A:
    def method(self):
        pass

class A_nested:
    class B:
        def method(self):
            pass
        
    class C:
        @staticmethod
        def method():
            pass

def global_function():
    pass

class TestGetClassThatDefinedMethod(unittest.TestCase):

    def test_builtin_function(self):
        self.assertIsNone(get_class_that_defined_method(len))

    def test_nested_class_method(self):
        instance = A_nested.B()
        self.assertEqual(get_class_that_defined_method(instance.method), A_nested.B)

    def test_function(self):
        self.assertIsNone(get_class_that_defined_method(global_function))

    def test_nested_class_function(self):
        self.assertEqual(get_class_that_defined_method(A_nested.C.method), A_nested.C)

    def test_nest_prefix(self):
        instance = A_nested.B()
        self.assertEqual(get_class_that_defined_method(instance.method), A_nested.B)

    def test_object_from_module(self):
        instance = A_nested.B()
        self.assertEqual(get_class_that_defined_method(instance.method), A_nested.B)

    def test_qualname_access(self):
        instance = A_nested.B()
        self.assertEqual(get_class_that_defined_method(instance.method), A_nested.B)

    def test_import_functools(self):
        mock_func = MagicMock()
        mock_func.partial = int
        with patch('builtins.__import__', return_value=mock_func) as mock_import:
            get_class_that_defined_method(global_function)
            self.assertIn('functools', mock_import.call_args.args)

    @patch('object_path.get_nest_prefix_by_qualname')
    @patch('object_path.get_object_from')
    def test_update_qualname_parsing(self, mock_get_obj, mock_get_nest_prefix):
        get_class_that_defined_method(global_function)
        mock_get_obj.assert_called()
        mock_get_nest_prefix.assert_called_with(global_function)

    @patch('object_path.get_object_from', return_value=None)
    def test_handle_none(self, mock_get_obj):
        get_class_that_defined_method(global_function)
        self.assertEqual(mock_get_obj.call_count, 2)

if __name__ == '__main__':
    unittest.main()
