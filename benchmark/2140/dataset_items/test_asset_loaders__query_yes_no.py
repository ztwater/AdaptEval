import unittest
from unittest.mock import patch

from asset_loaders import _query_yes_no, _assign_value_to_always_answer


class TestQueryYesNo(unittest.TestCase):

    def test_method_name_update(self):
        # 测试方法名是否更新为 _query_yes_no
        import asset_loaders
        self.assertTrue(callable(_query_yes_no))
        self.assertNotIn('query_yes_no', asset_loaders.__dict__)

    def test_add_global_variable_check(self):
        _assign_value_to_always_answer('predefined_answer')
        self.assertEqual(_query_yes_no("Do you agree?"), 'predefined_answer')
        _assign_value_to_always_answer(None)

    @patch('builtins.print')
    @patch('sys.stdout.write')
    @patch('builtins.input', return_value='y')
    def test_replace_sys_stdout_write_with_print(self, mock_input, mock_write, mock_print):
        _query_yes_no("Do you agree?")
        mock_write.assert_not_called()
        self.assertEqual(mock_print.call_args.args[0], "Do you agree? [Y/n] ")

    @patch('builtins.print')
    @patch('builtins.input', return_value='y')
    def test_add_end_argument(self, mock_input, mock_print):
        _query_yes_no("Do you agree?")
        self.assertIn('end', mock_print.call_args.kwargs)
        self.assertEqual(mock_print.call_args.kwargs['end'], "")

    @patch('builtins.input', return_value='')
    def test_default_yes(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertTrue(_query_yes_no("Do you agree?"))

    @patch('builtins.input', return_value='')
    def test_default_no(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertFalse(_query_yes_no("Do you agree?", default='no'))

    @patch('builtins.input', return_value='yes')
    def test_input_yes(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertTrue(_query_yes_no("Do you agree?"))

    @patch('builtins.input', return_value='ye')
    def test_input_yes_1(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertTrue(_query_yes_no("Do you agree?"))

    @patch('builtins.input', return_value='y')
    def test_input_yes_2(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertTrue(_query_yes_no("Do you agree?"))

    @patch('builtins.input', return_value='no')
    def test_input_no(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertFalse(_query_yes_no("Do you agree?"))

    @patch('builtins.input', return_value='n')
    def test_input_no_1(self, mock_input):
        _assign_value_to_always_answer(None)
        self.assertFalse(_query_yes_no("Do you agree?"))


if __name__ == '__main__':
    unittest.main()
