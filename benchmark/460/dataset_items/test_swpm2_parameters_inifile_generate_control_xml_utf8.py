import unittest
import os
import tempfile
from unittest.mock import patch, mock_open, MagicMock
from ansible.module_utils.basic import missing_required_lib

from swpm2_parameters_inifile_generate import control_xml_utf8, set_has_lxml_library


class TestControlXmlUtf8(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.filepath = self.test_dir.name

        # Create a temporary 'control.xml' file
        self.source_file = os.path.join(self.filepath, "control.xml")
        with open(self.source_file, 'wb') as f:
            f.write(b'<root>test</root>')

    def tearDown(self):
        # Clean up the temporary directory
        self.test_dir.cleanup()
        if os.path.exists("./control_utf8.xml"):
            os.remove("control_utf8.xml")

    @patch('lxml.etree.XMLParser')
    @patch('lxml.etree.parse')
    @patch('lxml.etree.tostring', return_value=b'<?xml version="1.0" encoding="UTF-8"?><root>test</root>')
    def test_control_xml_utf8(self, mock_tostring, mock_parse, mock_XMLParser):
        # Mocking module with fail_json method
        module = MagicMock()
        module.fail_json = MagicMock()

        # Call the function with the temporary filepath and mock module
        control_xml_utf8(self.filepath, module)

        # Check if the etree.parse was called with the opened file
        mock_parse.assert_called_once()

        # Check if the etree.tostring was called with correct parameters
        mock_tostring.assert_called_once()

        # Check if the output file was written correctly
        with open('control_utf8.xml', 'rb') as f:
            output_content = f.read()
        self.assertEqual(output_content,
                         b'<?xml version="1.0" encoding="UTF-8"?><root>test</root>'.decode('utf8').encode('iso-8859-1'))

    @patch('lxml.etree.XMLParser')
    @patch('lxml.etree.parse')
    @patch('lxml.etree.tostring', return_value=b'<?xml version="1.0" encoding="UTF-8"?><root>test</root>')
    def test_strip_cdata_argument_missing(self, mock_tostring, mock_parse, mock_XMLParser):
        # Mocking module with fail_json method
        module = MagicMock()
        module.fail_json = MagicMock()

        # Call the function with the temporary filepath and mock module
        control_xml_utf8(self.filepath, module)

        # Check if the XMLParser was initialized with correct encoding and strip_cdata parameter
        mock_XMLParser.assert_called_with(encoding="iso-8859-1", strip_cdata=False)

    def test_control_xml_utf8_library_missing(self):
        # Simulate the library not being available
        set_has_lxml_library(False)

        # Mocking module with fail_json method
        module = MagicMock()
        module.fail_json = MagicMock()

        # Call the function with a sample filepath and mock module
        control_xml_utf8(self.filepath, module)

        # Check if fail_json was called due to missing library
        module.fail_json.assert_called_with(msg=missing_required_lib("lxml"),
                                            exception=None)

        # Reset global variable
        set_has_lxml_library(True)

    @patch('lxml.etree.XMLParser')
    @patch('lxml.etree.parse')
    @patch('lxml.etree.tostring', return_value=b'<?xml version="1.0" encoding="UTF-8"?><root>test</root>')
    def test_target_path_change(self, mock_tostring, mock_parse, mock_XMLParser):
        # Mocking module with fail_json method
        module = MagicMock()
        module.fail_json = MagicMock()

        # Call the function with the temporary filepath and mock module
        control_xml_utf8(self.filepath, module)

        # Check if the output file was create correctly
        self.assertTrue(os.path.exists('control_utf8.xml'), f"The path control_utf8.xml should exist.")

    def test_encapsulate(self):
        from swpm2_parameters_inifile_generate import control_xml_utf8, set_has_lxml_library

    def test_rename_output_file(self):
        # Mocking module with fail_json method
        module = MagicMock()
        module.fail_json = MagicMock()
        # Call the function with the temporary filepath and mock module
        control_xml_utf8(self.filepath, module)
        self.assertIn('control_utf8.xml', os.listdir('./'))


if __name__ == '__main__':
    unittest.main()

