import inspect
import unittest
from unittest.mock import patch
import os

from stretch_demo_base_env import StretchDemoBaseEnv

class TestRecursiveListdir(unittest.TestCase):

    def setUp(self):
        self.obj = StretchDemoBaseEnv()

        # Create a temporary directory structure for testing
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, 'sub_dir'), exist_ok=True)
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write('test file 1')
        with open(os.path.join(self.test_dir, 'sub_dir', 'file2.txt'), 'w') as f:
            f.write('test file 2')

    def tearDown(self):
        # Clean up the temporary directory structure
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_functional_correctness(self):
        expected_files = [
            os.path.join(self.test_dir, 'file1.txt'),
            os.path.join(self.test_dir, 'sub_dir', 'file2.txt')
        ]
        result_files = self.obj._recursive_listdir(self.test_dir)
        self.assertCountEqual(result_files, expected_files)

    def test_encapsulate(self):
        self.assertTrue(getattr(StretchDemoBaseEnv, '_recursive_listdir'))
        self.assertTrue(callable(StretchDemoBaseEnv._recursive_listdir))
        parameters = inspect.signature(StretchDemoBaseEnv._recursive_listdir).parameters
        self.assertIn('self', parameters)

    @patch('os.walk', return_value=[])
    def test_replace_hardcoded_path(self, mock_walk):
        parameters = inspect.signature(StretchDemoBaseEnv._recursive_listdir).parameters
        self.assertIn('directory', parameters)
        self.obj._recursive_listdir(self.test_dir)
        mock_walk.assert_called_with(self.test_dir)

    def test_return(self):
        result_files = self.obj._recursive_listdir(self.test_dir)
        self.assertIsInstance(result_files, list)

if __name__ == '__main__':
    unittest.main()
