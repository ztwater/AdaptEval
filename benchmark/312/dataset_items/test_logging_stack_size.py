import unittest
from unittest.mock import patch, MagicMock, call
from ctx_logging import stack_size

# A helper function to test stack_size with different levels of nesting
def test_helper(level):
    return stack_size()

class TestStackSize(unittest.TestCase):

    def test_rename_method(self):
        from ctx_logging import stack_size

    def test_stack_size_at_level_1(self):
        # Test stack size when called directly (no nesting)
        self.assertEqual(stack_size(), 1 + 2 + 9 + 7) # test stack have its own nesting level

    def test_stack_size_at_level_2(self):
        # Test stack size when called from another function
        def another_function():
            return stack_size()
        self.assertEqual(another_function(), 2 + 2 + 9 + 7)
    
    def test_stack_size_at_level_3(self):
        # Test stack size with two levels of nesting
        def middle_function():
            return test_helper(3)
        self.assertEqual(middle_function(), 3 + 2 + 9 + 7)
    
    def test_stack_size_with_custom_size_hint(self):
        # Test stack size with a custom size hint
        self.assertEqual(stack_size(size=3), 1 + 3 + 8 + 7)

    def test_stack_size_with_custom_size_hint_at_level_2(self):
        # Test stack size when called from another function
        def another_function():
            return stack_size(size=3)
        self.assertEqual(another_function(), 2 + 3 + 8 + 7)
    
    def test_stack_size_fallback(self):
        # Test the fallback mechanism when sys._getframe() fails
        self.assertEqual(stack_size(size=9999), 9)

    @patch('ctx_logging.count', return_value=[])
    def test_zero_stack_size(self, mock_count):
        result = stack_size(0)
        mock_count.assert_has_calls([call(0)])
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
