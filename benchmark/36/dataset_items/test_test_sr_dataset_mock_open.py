import inspect
import re
import unittest
from test_sr_dataset import mock_open

class TestMockOpen(unittest.TestCase):

    def test_mock_open_iteration(self):
        """Test that mock_open supports iteration."""
        data = "line1\nline2\nline3\n"
        m_open = mock_open(read_data=data)
        with m_open() as f:
            lines = list(f)
        self.assertEqual(lines, ["line1\n", "line2\n", "line3\n"])

    def test_mock_open_readline(self):
        """Test that mock_open readline works as expected."""
        data = "line1\nline2\nline3\n"
        m_open = mock_open(read_data=data)
        with m_open() as f:
            first_line = f.readline()
        self.assertEqual(first_line, "line1\n")

    def test_mock_open_read(self):
        """Test that mock_open read works as expected."""
        data = "line1\nline2\nline3\n"
        m_open = mock_open(read_data=data)
        with m_open() as f:
            content = f.read()
        self.assertEqual(content, data)

    def test_rename_parameter(self):
        parameters = inspect.signature(mock_open).parameters
        self.assertNotIn('kargs', parameters)
        self.assertIn('kwargs', parameters)

    def test_add_import(self):
        source = inspect.getsource(mock_open)
        matched_import = re.search(r'import\s+unittest\.mock', source)
        self.assertIsNotNone(matched_import)


if __name__ == '__main__':
    unittest.main()
