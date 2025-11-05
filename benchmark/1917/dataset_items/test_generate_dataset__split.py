import unittest

from generate_dataset import _split
 
class TestSplit(unittest.TestCase):

    def test_split_even_chunks(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        n = 4
        expected = [[1, 2], [3, 4], [5, 6], [7, 8]]
        result = _split(a, n)
        self.assertEqual(result, expected)

    def test_return_val_2_matrix(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        n = 4 
        result = _split(a, n)
        self.assertEqual(len(result), 4)

    def test_split_odd_chunks(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        expected = [[1, 2, 3], [4, 5], [6, 7]]
        result = _split(a, n)
        self.assertEqual(result, expected)

    def test_split_single_chunk(self):
        a = [1, 2, 3, 4, 5]
        n = 1
        expected = [[1, 2, 3, 4, 5]]
        result = _split(a, n)
        self.assertEqual(result, expected)

    def test_split_more_chunks_than_elements(self):
        a = [1, 2, 3]
        n = 5
        expected = [[1], [2], [3], [], []]
        result = _split(a, n)
        self.assertEqual(result, expected)

    def test_split_empty_list(self):
        a = []
        n = 3
        expected = [[], [], []]
        result = _split(a, n)
        self.assertEqual(result, expected)

    def test_rename_function(self):
        import generate_dataset
        self.assertTrue(callable(_split))
        self.assertNotIn('split', generate_dataset.__dict__)

    def test_convert_return(self):
        a = [1, 2, 3, 4, 5]
        n = 1
        expected = [[1, 2, 3, 4, 5]]
        result = _split(a, n)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, tuple)

if __name__ == '__main__':
    unittest.main()