import unittest
import inspect
from xml.etree.ElementTree import Element
from xml.etree import ElementTree as ET
from ctx_types import xml_to_dict_recursive

class TestXmlToDictRecursive(unittest.TestCase):

    def setUp(self):
        # Sample XML string for testing
        self.xml_str = '''
        <root>
            <child1>Text1</child1>
            <child2 attr="value">Text2</child2>
            <child3>
                <subchild1>Subtext1</subchild1>
            </child3>
        </root>
        '''
        self.root = ET.fromstring(self.xml_str)

    def test_simple_text_node(self):
        # Test for a simple text node
        child1 = self.root.find('child1')
        result = xml_to_dict_recursive(child1)
        expected = {'child1': 'Text1'}
        self.assertEqual(result, expected, "The text node should be converted correctly.")

    def test_node_with_attribute(self):
        # Test for a node with an attribute
        child2 = self.root.find('child2')
        result = xml_to_dict_recursive(child2)
        # Note: The provided function does not handle attributes, so this test expects failure.
        expected = {'child2': 'Text2'}
        self.assertEqual(result, expected, "The node with attribute should be converted correctly.")

    def test_nested_elements(self):
        # Test for nested elements
        child3 = self.root.find('child3')
        result = xml_to_dict_recursive(child3)
        expected = {'child3': [{'subchild1': 'Subtext1'}]}
        self.assertEqual(result, expected, "The nested elements should be converted correctly.")

    def test_empty_element(self):
        # Test for an empty element
        empty_element = ET.Element('empty')
        result = xml_to_dict_recursive(empty_element)
        expected = {'empty': None}
        self.assertEqual(result, expected, "The empty element should be converted to None.")

    def test_multiple_children(self):
        # Test for multiple child elements
        result = xml_to_dict_recursive(self.root)
        expected = {
            'root': [
                {'child1': 'Text1'},
                {'child2': 'Text2'},
                {'child3': [{'subchild1': 'Subtext1'}]}
            ]
        }
        self.assertEqual(result, expected, "Multiple child elements should be converted correctly.")

    def test_type_annotation_root_parameter(self):
        # Test for type annotation of the root parameter
        annotations = xml_to_dict_recursive.__annotations__
        self.assertIn('root', annotations)
        self.assertEqual(annotations['root'], Element)

    def test_return_type_annotation(self):
        # Test for the return type annotation of the function
        annotations = xml_to_dict_recursive.__annotations__
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], dict)

if __name__ == '__main__':
    unittest.main()
