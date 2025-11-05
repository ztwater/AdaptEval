import unittest
from typing import List, TypeVar
import inspect

from util import list_split, T


class TestListSplit(unittest.TestCase):
    def test_split_equal_chunks(self):
        result = list_split([1, 2, 3, 4], 2)
        self.assertEqual(result, [[1, 2], [3, 4]])

    def test_split_unequal_chunks(self):
        result = list_split([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, [[1, 2], [3, 4], [5]])

    def test_split_single_element_chunks(self):
        result = list_split([1, 2, 3], 3)
        self.assertEqual(result, [[1], [2], [3]])

    def test_split_more_chunks_than_elements(self):
        result = list_split([1, 2], 4)
        self.assertEqual(result, [[1], [2], [], []])

    def test_split_empty_list(self):
        result = list_split([], 3)
        self.assertEqual(result, [[], [], []])

    def test_split_into_one_chunk(self):
        result = list_split([1, 2, 3, 4, 5], 1)
        self.assertEqual(result, [[1, 2, 3, 4, 5]])

    def test_rename_parameter(self):
        signature = inspect.signature(list_split)
        parameters = signature.parameters
        self.assertEqual("l", list(parameters.keys())[0])

    def test_add_type_annotations(self):
        annotations = list_split.__annotations__
        self.assertIn('l', annotations)
        self.assertEqual(annotations['l'], List[T])
        self.assertIn('n', annotations)
        self.assertEqual(annotations['n'], int)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], List[List[T]])

    def test_change_return_value(self):
        result = list_split([], 3)
        self.assertEqual(type(result), list)
        self.assertNotEqual(type(result), tuple)


if __name__ == '__main__':
    unittest.main()
