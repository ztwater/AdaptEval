import os
import unittest
from unittest.mock import patch
from invoker import check_root_privileges

class TestCheckRootPrivileges(unittest.TestCase):
    def test_not_root_raises_permission_error(self):
        # Mock os.environ.get to return None and os.geteuid to return a non-zero value
        with patch.dict('os.environ', dict()):
            with patch('os.geteuid', return_value=1000):
                with self.assertRaises(PermissionError):
                    check_root_privileges()

    def test_root_does_not_raise_permission_error(self):
        # Mock os.environ.get to return a non-None value and os.geteuid to return 0
        with patch.dict('os.environ', {'SUDO_UID': '1234'}):  # Example SUDO_UID value
            with patch('os.geteuid', return_value=0):
                try:
                    check_root_privileges()
                except PermissionError:
                    self.fail("check_root_privileges() raised PermissionError unexpectedly!")

    def test_rename_function(self):
        from invoker import check_root_privileges
        self.assertTrue(callable(check_root_privileges), "Function 'check_root_privileges' not found.")

    def test_return_type_none(self):
        # Check if the return type annotation is 'NoneType'
        annotations = check_root_privileges.__annotations__
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], None)

if __name__ == "__main__":
    unittest.main()
