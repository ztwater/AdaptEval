import inspect
import os
import shutil
import unittest
from os_Utils import mkdir_recursive

class TestMkdirRecursive(unittest.TestCase):
    def setUp(self):
        """Set up a temporary directory for testing."""
        self.test_dir = "test_dir"
        if not os.path.exists(self.test_dir):
            os.mkdir(self.test_dir)

    def tearDown(self):
        """Clean up the temporary directory after testing."""
        shutil.rmtree(self.test_dir)  # Assumes the directory is empty after tests

    def test_mkdir_recursive_creates_new_directory(self):
        """Test that a new directory is created."""
        new_dir = os.path.join(self.test_dir, "new_subdir")
        self.assertFalse(os.path.exists(new_dir))  # Check that the directory does not exist before the test
        mkdir_recursive(new_dir)
        self.assertTrue(os.path.exists(new_dir))  # Check that the directory exists after the test

    def test_mkdir_recursive_existing_directory(self):
        """Test that the function does not raise an error if the directory already exists."""
        existing_dir = os.path.join(self.test_dir, "existing_subdir")
        os.mkdir(existing_dir)
        # Call mkdir_recursive on an existing directory
        try:
            mkdir_recursive(existing_dir)
        except OSError as e:
            self.fail(f"mkdir_recursive raised an unexpected OSError: {e}")

    def test_mkdir_recursive_nested_directory(self):
        """Test that nested directories are created."""
        nested_dir = os.path.join(self.test_dir, "nested", "subdir")
        self.assertFalse(os.path.exists(nested_dir))  # Check that the nested directory does not exist before the test
        mkdir_recursive(nested_dir)
        self.assertTrue(os.path.exists(nested_dir))  # Check that the nested directory exists after the test

    def test_rename_method(self):
        from os_Utils import mkdir_recursive

    def test_remove_self_reference(self):
        parameters = inspect.signature(mkdir_recursive).parameters
        self.assertNotIn('self', parameters)


if __name__ == '__main__':
    unittest.main()