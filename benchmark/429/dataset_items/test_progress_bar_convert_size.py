import unittest

from progress_bar import convert_size

class TestConvertSize(unittest.TestCase):

    def test_convert_size_zero(self):
        # Test that zero bytes returns "0B"
        self.assertEqual(convert_size(0), "0B")

    def test_convert_size_bytes(self):
        # Test conversion within the bytes range
        self.assertEqual(convert_size(512), (512, 'B'))

    def test_convert_size_kilobytes(self):
        # Test conversion within the kilobytes range
        self.assertEqual(convert_size(2048), (2.0, 'KB'))

    def test_convert_size_megabytes(self):
        # Test conversion within the megabytes range
        self.assertEqual(convert_size(1048576), (1.0, 'MB'))

    def test_convert_size_gigabytes(self):
        # Test conversion within the gigabytes range
        self.assertEqual(convert_size(1073741824), (1.0, 'GB'))

    def test_convert_size_terabytes(self):
        # Test conversion within the terabytes range
        self.assertEqual(convert_size(1099511627776), (1.0, 'TB'))

    def test_return_type(self):
        # Test that the return type is a tuple for non-zero input
        result = convert_size(1024)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], float)
        self.assertIsInstance(result[1], str)

if __name__ == '__main__':
    unittest.main()

