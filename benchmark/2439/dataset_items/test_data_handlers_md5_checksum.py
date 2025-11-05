import unittest
import hashlib
import os

from data_handlers import md5_checksum   

class TestMd5Checksum(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file_path = 'test_file.tmp'
        with open(self.test_file_path, 'w') as f:
            f.write('Hello, World!')

    def tearDown(self):
        os.remove(self.test_file_path)

    def test_method_signature(self):
        # Check the function signature for correct parameter types
        from inspect import signature
        sig = signature(md5_checksum)
        params = sig.parameters

        self.assertEqual(params['filepath'].annotation, str)
        self.assertEqual(sig.return_annotation, str)

    def test_function_rename(self):
        # Ensure the function name is correctly updated
        import data_handlers
        self.assertTrue(callable(md5_checksum))
        self.assertNotIn('md5', data_handlers.__dict__)
        self.assertEqual(md5_checksum, data_handlers.__dict__['md5_checksum'])

    def test_rename_parameter(self):
        from inspect import signature
        sig = signature(md5_checksum)
        params = sig.parameters
        self.assertNotIn('fname', params)
        self.assertIn('filepath', params)

    def test_md5_checksum_correct(self):
        # Calculate the MD5 checksum of the test file
        result = md5_checksum(self.test_file_path)
        # The expected MD5 checksum for 'Hello, World!'
        expected_checksum = '65a8e27d8879283831b664bd8b7f0ad4'
        self.assertEqual(result, expected_checksum)

    def test_md5_checksum_empty_file(self):
        # Create an empty file for testing
        empty_file_path = 'empty_file.tmp'
        with open(empty_file_path, 'w') as f:
            pass

        # Calculate the MD5 checksum of the empty file
        result = md5_checksum(empty_file_path)
        # The expected MD5 checksum for an empty string
        expected_checksum = 'd41d8cd98f00b204e9800998ecf8427e'
        self.assertEqual(result, expected_checksum)
        os.remove(empty_file_path)

    def test_md5_checksum_nonexistent_file(self):
        # Attempt to calculate the MD5 checksum of a nonexistent file
        with self.assertRaises(FileNotFoundError):
            md5_checksum('nonexistent_file.tmp')

    def test_md5_checksum_large_file(self):
        # Create a large file for testing
        large_file_path = 'large_file.tmp'
        with open(large_file_path, 'w') as f:
            for _ in range(1000):
                f.write('This is a large file used for testing the MD5 checksum function.\n')

        # Calculate the MD5 checksum of the large file
        result = md5_checksum(large_file_path)
        # We cannot assert the exact checksum here since it depends on the content
        # However, we can assert that the result is a valid MD5 hash
        self.assertEqual(len(result), 32)
        self.assertTrue(all(c in '0123456789abcdef' for c in result))
        os.remove(large_file_path)

if __name__ == '__main__':
    unittest.main()
