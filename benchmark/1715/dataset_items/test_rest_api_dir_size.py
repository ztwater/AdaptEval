import unittest
import os
import inspect
import shutil
from tempfile import mkdtemp, mkstemp

from rest_api import HddStatsViewSet

class TestDirSize(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = mkdtemp()
        # Create some files within the test directory with known sizes
        self.file_sizes = [1024, 2048, 4096]  # Example file sizes in bytes
        self.filenames = []
        for size in self.file_sizes:
            _, filename = mkstemp(dir=self.test_dir)
            self.filenames.append(filename)
            with open(filename, 'wb') as f:
                f.write(b'x' * size)
        self.obj = HddStatsViewSet()

    def test_add_method_parameter(self):
        parameters = inspect.signature(HddStatsViewSet.dir_size).parameters
        self.assertIn('self', parameters)

    def test_rename_function(self):
        self.assertTrue(hasattr(HddStatsViewSet, 'dir_size'))
        self.assertTrue(callable(self.obj.dir_size))

    def test_rename_parameter(self):
        parameters = inspect.signature(HddStatsViewSet.dir_size).parameters
        self.assertIn("d", parameters)
        self.assertNotIn("start_path", parameters)

    def test_remove_default_value(self):
        parameters = inspect.signature(HddStatsViewSet.dir_size).parameters
        self.assertEqual(parameters["d"].default, inspect.Parameter.empty)

    def test_variable_names(self):
        self.assertIn("size", HddStatsViewSet.dir_size.__code__.co_varnames)
        self.assertNotIn("total_size", HddStatsViewSet.dir_size.__code__.co_varnames)

    def test_valid_directory_size(self):
        size = 0
        for filename in self.filenames:
            size += os.path.getsize(filename)
        self.assertEqual(self.obj.dir_size(self.test_dir), size)

    def test_dir_size_with_files(self):
        # Test that the dir_size method correctly calculates the size of the directory
        calculated_size = self.obj.dir_size(self.test_dir)
        expected_size = sum(self.file_sizes)
        self.assertEqual(calculated_size, expected_size)

if __name__ == '__main__':
    unittest.main()
