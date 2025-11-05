import unittest
from typing import Generator
from models import ImportInfo
from parsers import get_module_info_from_python_file
from unittest.mock import mock_open, patch, MagicMock
import ast
import os

class TestGetModuleInfoFromPythonFile(unittest.TestCase):
    def setUp(self):
        self.file_content_without_imports = "print('No imports here')"
        # Create a mock file content with import statements
        self.mock_file_content = """
from coco import bunny
from coco.bungy import carrot
from meta import teta
from rocket import spaceship as sp
import bingo
import com.stackoverflow
import motorbike as car
import module1, module2
        """
        # Use mock_open to simulate opening a file
        self.mock_file = mock_open(read_data=self.mock_file_content)

        self.yield_path = 'test_yield.py'
        self.empty_module_path = 'test_empty_module.py'

    def tearDown(self):
        if os.path.exists(self.yield_path):
            os.remove(self.yield_path)
        if os.path.exists(self.empty_module_path):
            os.remove(self.empty_module_path)

    # function test
    def test_get_module_info_from_python_file(self):
        # Use patch to replace the built-in open function with mock_open
        with patch('builtins.open', self.mock_file):
            # Call the function with the path to the mock file
            imports = list(get_module_info_from_python_file('dummy_path.py'))
            
            # Define the expected results
            expected_imports = [
                ImportInfo(module=['coco'], name=['bunny'], alias=None),
                ImportInfo(module=['coco', 'bungy'], name=['carrot'], alias=None),
                ImportInfo(module=['meta'], name=['teta'], alias=None),
                ImportInfo(module=['rocket'], name=['spaceship'], alias='sp'),
                ImportInfo(module=[], name=['bingo'], alias=None),
                ImportInfo(module=[], name=['com', 'stackoverflow'], alias=None),
                ImportInfo(module=[], name=['motorbike'], alias='car'),
                ImportInfo(module=[], name=['module1'], alias=None),
                ImportInfo(module=[], name=['module2'], alias=None)
            ]
            
            # Check if the actual results match the expected results
            self.assertEqual(imports, expected_imports)

    def test_type_annotations(self):
        # Test that the function has the correct type annotations
        self.assertEqual(get_module_info_from_python_file.__annotations__, {
            'path': str, 'return': Generator[ImportInfo, None, None]
        })

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="from . import something\n")
    def test_encoding_specification(self, mock_open):
        dummy_path = 'dummy_file.py'
        imports = list(get_module_info_from_python_file(dummy_path))
        mock_open.assert_called_with(dummy_path, encoding='utf-8')

    def test_empty_module_handling(self):
        path = self.empty_module_path
        with open(path, 'w', encoding='utf-8') as f:
            f.write("from . import something\n")
        imports = list(get_module_info_from_python_file(path))
        self.assertEqual(imports[0].module, [])

    def test_yield_statement_update(self):
        path = self.yield_path
        with open(path, 'w', encoding='utf-8') as f:
            f.write("import os\n")
        imports = list(get_module_info_from_python_file(path))
        self.assertIsInstance(imports[0], ImportInfo)

    def test_node_without_names_attribute(self):
        # Create a mock node without 'names' attribute
        node_without_names = MagicMock(spec=ast.Import)
        # print(node_without_names.names)
        with patch('builtins.open', mock_open(read_data=self.file_content_without_imports)) as mock_file, patch('ast.parse', return_value=MagicMock(body=[node_without_names])), patch('ast.iter_child_nodes', return_value=list([node_without_names])):
            imports = list(get_module_info_from_python_file('dummy_path.py'))
        self.assertEqual(imports, [])


if __name__ == '__main__':
    unittest.main()