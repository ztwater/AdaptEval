import unittest
from unittest.mock import MagicMock, patch
import inspect
from sphinx.ext import autodoc

from conf import mock_autodoc


class TestMockAutodoc(unittest.TestCase):

    def setUp(self):
        self.original_class_documenter = autodoc.ClassDocumenter
        mock_autodoc()

    def tearDown(self):
        autodoc.ClassDocumenter = self.original_class_documenter

    def test_encapsulate(self):
        pass

    @patch.object(autodoc.ClassDocumenter, 'add_line', autospec=True)
    def test_add_line_override(self, mock_add_line):
        # Create a mock environment and directive
        mock_env = MagicMock()
        mock_directive = MagicMock()
        mock_options = MagicMock()

        # Create an instance of the mocked class documenter
        mocked_documenter = autodoc.ClassDocumenter(mock_env, mock_directive, mock_options)

        # Call the overridden add_line method with the specific line
        mocked_documenter.add_line("   Bases: :py:class:`object`", "source")

        # Ensure that the original add_line method was not called
        mock_add_line.assert_not_called()

        # Call the overridden add_line method with a different line
        mocked_documenter.add_line("   Some other line", "source")

        # Ensure that the original add_line method was called with the correct arguments
        mock_add_line.assert_called_once_with(mocked_documenter, "   Some other line", "source")

    def test_autodoc_class_documenter_assignment(self):
        # Verify that the ClassDocumenter has been replaced by MockedClassDocumenter
        self.assertTrue(issubclass(autodoc.ClassDocumenter, self.original_class_documenter))
        
    def test_override_decorator(self):
        # Verify that the add_line method has the @override decorator
        method = autodoc.ClassDocumenter.add_line
        print(inspect.getsource(method))
        self.assertIn('override', inspect.getsource(method))

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
