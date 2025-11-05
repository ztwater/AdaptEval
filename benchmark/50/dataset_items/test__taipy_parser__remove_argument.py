import inspect
import re
import unittest
import argparse
from typing import Dict

from _taipy_parser import _TaipyParser


class TestRemoveArgument(unittest.TestCase):
    def setUp(self):
        self.source = inspect.getsource(_TaipyParser._remove_argument)

        _TaipyParser._parser = argparse.ArgumentParser(conflict_handler="resolve")
        _TaipyParser._sub_taipyparsers = {}
        _TaipyParser._arg_groups = {}
        _TaipyParser._parser.add_argument('--foo', dest='foo')
        _TaipyParser._parser.add_argument('--bar', dest='bar')

    def test_remove_existing_argument(self):
        _TaipyParser._remove_argument('foo')
        actions = [action.dest for action in _TaipyParser._parser._actions]
        self.assertNotIn('foo', actions)
        self.assertIn('bar', actions)

    def test_remove_non_existing_argument(self):
        _TaipyParser._remove_argument('baz')
        actions = [action.dest for action in _TaipyParser._parser._actions]
        self.assertIn('foo', actions)
        self.assertIn('bar', actions)

    def test_remove_argument_from_group(self):
        group = _TaipyParser._parser.add_argument_group('group')
        group.add_argument('--baz', dest='baz')
        _TaipyParser._remove_argument('baz')
        group_actions = [action.dest for group in _TaipyParser._parser._action_groups for action in group._group_actions]
        self.assertNotIn('baz', group_actions)
        actions = [action.dest for action in _TaipyParser._parser._actions]
        self.assertIn('foo', actions)
        self.assertIn('bar', actions)

    def test_type_annotation(self):
        self.assertTrue(hasattr(_TaipyParser._remove_argument, '__annotations__'))
        self.assertEqual(_TaipyParser._remove_argument.__annotations__['arg'], str)

    def test_update_method_name_and_type(self):
        _TaipyParser._remove_argument('foo')

    def test_change_parameter_name(self):
        parameters = inspect.signature(_TaipyParser._remove_argument).parameters
        self.assertNotIn('parser', parameters)

    def test_change_attribute_access(self):
        matched_attr = re.search(r'\bcls\._parser', self.source)
        self.assertIsNotNone(matched_attr)

    def test_refactor_identifier(self):
        matched_old = re.search(r'for\s+action\s+in\s+(cls\._)?parser\._action_groups:', self.source)
        matched_new = re.search(r'for\s+argument_group\s+in\s+(cls\._)?parser\._action_groups', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

if __name__ == '__main__':
    unittest.main()
