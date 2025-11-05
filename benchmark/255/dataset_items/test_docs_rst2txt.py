import re
import unittest
from unittest.mock import patch
import types
from typing import cast
import inspect

from docs import rst2txt


class TestRst2txt(unittest.TestCase):
    def setUp(self):
        self.valid_rst = """
Hello World
============

This is a simple example of reStructuredText.
"""
        self.source = inspect.getsource(rst2txt)

    def test_change_method_signature(self):
        rst2txt("Hello world.")

    def test_rename_parameter(self):
        signature = inspect.signature(rst2txt)
        parameters = signature.parameters
        self.assertEqual("source", list(parameters.keys())[0])

    @patch('logging.warning')
    def test_add_exception_handling(self, mock_logging_warning):
        # Test the exception handling logic
        invalid_rst = 12345
        # Test that logging occurs as expected during an exception
        with patch('builtins.print', side_effect=Exception("Error during conversion")):
            original = rst2txt(invalid_rst)
        mock_logging_warning.assert_called_once()
        self.assertEqual(rst2txt(invalid_rst), 12345)

    def test_add_imports(self):
        matched_import_0 = re.search(r'import\s*docutils\.nodes|'
                                     r'from\s*docutils\s*import\s*node',
                                     self.source)
        matched_import_1 = re.search(r'import\s*docutils\.parsers\.rst|'
                                     r'from\s*docutils\.parsers\s*import\s*rst',
                                     self.source)
        matched_import_2 = re.search(r'import\s*docutils\.utils|'
                                     r'from\s*docutils\s*import\s*utils',
                                     self.source)
        matched_import_3 = re.search(r'import\s*sphinx\.writers\.text|'
                                     r'from\s*sphinx\.writers\s*import\s*text',
                                     self.source)
        matched_import_4 = re.search(r'import\s*sphinx\.builders\.text|'
                                     r'from\s*sphinx\.builders\s*import\s*text',
                                     self.source)
        matched_import_5 = re.search(r'import\s*sphinx\.util\.osutil|'
                                     r'from\s*sphinx\.util\s*import\s*osutil',
                                     self.source)
        self.assertIsNotNone(matched_import_0)
        self.assertIsNotNone(matched_import_1)
        self.assertIsNotNone(matched_import_2)
        self.assertIsNotNone(matched_import_3)
        self.assertIsNotNone(matched_import_4)
        self.assertIsNotNone(matched_import_5)

    def test_import_sphinx_application(self):
        matched_imports = re.search(r'from\s*sphinx\.application\s*import\s*Sphinx|'
                                    r'import\s*sphinx\.application\.Sphinx',
                                    self.source)
        self.assertIsNotNone(matched_imports)

    def test_type_casting_for_sphinx_application(self):
        # cast is a no-op at runtime, so we still match it with re
        matched_cast = re.search(r'cast\((Sphinx|sphinx\.application\.Sphinx),.+\)', self.source)
        self.assertIsNotNone(matched_cast)

    @patch('warnings.catch_warnings')
    def test_add_warning_handling(self, mock_catch_warnings):
        # Test that warnings are caught during the conversion
        with patch('sphinx.builders.text.TextBuilder', side_effect=RuntimeWarning("Warning during conversion")):
            rst2txt("Some valid reStructuredText")
        mock_catch_warnings.assert_called()

    def test_add_events_parameter(self):
        with patch('types.SimpleNamespace', return_value=None) as mock_simplespace:
            result = rst2txt("Hello world.")
            actual_args, actual_kwargs = mock_simplespace.call_args
            self.assertIn('events', actual_kwargs)
            self.assertEqual(actual_kwargs['events'], None)

    def test_combine_code_blocks(self):
        result = rst2txt("Hello world.")
        self.assertIsInstance(result, str)  # Assuming the result should be a string
        self.assertEqual(result, "Hello world.\n")

    def test_rename_identifier(self):
        matched_rename = re.search(r'_app\s*=\s*types\.SimpleNamespace', self.source)
        self.assertIsNotNone(matched_rename)

if __name__ == '__main__':
    unittest.main()
