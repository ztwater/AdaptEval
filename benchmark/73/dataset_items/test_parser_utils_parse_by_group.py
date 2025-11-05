import unittest
from unittest.mock import patch
from argparse import ArgumentParser, Namespace

from parser_utils import parse_by_group 

class TestParseByGroup(unittest.TestCase):
    def setUp(self):
        self.parser = ArgumentParser()
        self.parser.add_argument('pos_arg', type=int, help='A positional argument')
        self.parser.add_argument('--opt_arg', type=str, help='An optional argument')

        group1 = self.parser.add_argument_group('group1')
        group1.add_argument('--g1_arg1', type=str, help='Group 1 argument 1')
        group1.add_argument('--g1_arg2', type=int, help='Group 1 argument 2')

        group2 = self.parser.add_argument_group('group2')
        group2.add_argument('--g2_arg1', type=float, help='Group 2 argument 1')

    @patch('sys.argv', ['script_name', '10', '--opt_arg', 'test'])
    def test_positional_and_optional_arguments(self):
        namespace = parse_by_group(self.parser)
        self.assertEqual(namespace.pos_arg, 10)
        self.assertEqual(namespace.opt_arg, 'test')

    @patch('sys.argv', ['script_name', '10', '--opt_arg', 'test', '--g1_arg1', 'group1_value', '--g1_arg2', '5'])
    def test_group_arguments(self):
        namespace = parse_by_group(self.parser)
        self.assertEqual(namespace.group1.g1_arg1, 'group1_value')
        self.assertEqual(namespace.group1.g1_arg2, 5)

    @patch('sys.argv', ['script_name', '10', '--opt_arg', 'test', '--g2_arg1', '3.14'])
    def test_flat_argument(self):
        namespace = parse_by_group(self.parser)
        self.assertTrue(hasattr(namespace, 'flat'))
        self.assertEqual(namespace.flat.pos_arg, 10)
        self.assertEqual(namespace.flat.opt_arg, 'test')
        self.assertEqual(namespace.flat.g2_arg1, 3.14)

    @patch('sys.argv', ['script_name', '10', '--opt_arg', 'test', '--g1_arg1', 'group1_value', '--g1_arg2', '5', '--g2_arg1', '3.14'])
    def test_combined_arguments(self):
        namespace = parse_by_group(self.parser)
        self.assertEqual(namespace.pos_arg, 10)
        self.assertEqual(namespace.opt_arg, 'test')
        self.assertEqual(namespace.group1.g1_arg1, 'group1_value')
        self.assertEqual(namespace.group1.g1_arg2, 5)
        self.assertEqual(namespace.group2.g2_arg1, 3.14)
        self.assertTrue(hasattr(namespace, 'flat'))
        self.assertEqual(namespace.flat.pos_arg, 10)
        self.assertEqual(namespace.flat.opt_arg, 'test')
        self.assertEqual(namespace.flat.g1_arg1, 'group1_value')
        self.assertEqual(namespace.flat.g1_arg2, 5)
        self.assertEqual(namespace.flat.g2_arg1, 3.14)

    @patch('sys.argv', ['script_name', '10', '--opt_arg', 'test'])
    def test_method_renaming(self):
        namespace = parse_by_group(self.parser)

    @patch('sys.argv', ['script_name', '10', '--opt_arg', 'test'])
    def test_add_flat_argument(self):
        namespace = parse_by_group(self.parser)
        self.assertTrue(hasattr(namespace, 'flat'))

if __name__ == '__main__':
    unittest.main()

