import unittest
from xml.etree.ElementTree import Element
from collections import defaultdict
import inspect

from xrdml import etree_to_dict

class TestEtreeToDict(unittest.TestCase):

    def test_element_with_no_children_or_attributes(self):
        e = Element('root')
        expected = {'root': None}
        self.assertEqual(etree_to_dict(e), expected)

    def test_element_with_text_only(self):
        e = Element('root')
        e.text = 'some text'
        expected = {'root': 'some text'}
        self.assertEqual(etree_to_dict(e), expected)

    def test_element_with_attributes_only(self):
        e = Element('root', attrib={'key': 'value'})
        expected = {'root': {'@key': 'value'}}
        self.assertEqual(etree_to_dict(e), expected)

    def test_element_with_children(self):
        root = Element('root')
        child1 = Element('child')
        child1.text = 'child1 text'
        child2 = Element('child')
        child2.text = 'child2 text'
        root.extend([child1, child2])
        
        expected = {
            'root': {
                'child': ['child1 text', 'child2 text']
            }
        }
        self.assertEqual(etree_to_dict(root), expected)

    def test_element_with_children_and_attributes(self):
        root = Element('root', attrib={'key': 'value'})
        child = Element('child')
        child.text = 'child text'
        root.append(child)
        
        expected = {
            'root': {
                '@key': 'value',
                'child': 'child text'
            }
        }
        self.assertEqual(etree_to_dict(root), expected)

    def test_element_with_children_attributes_and_text(self):
        root = Element('root', attrib={'key': 'value'})
        child = Element('child')
        child.text = 'child text'
        root.append(child)
        root.text = 'root text'
        
        expected = {
            'root': {
                '@key': 'value',
                'child': 'child text',
                '#text': 'root text'
            }
        }
        self.assertEqual(etree_to_dict(root), expected)

    def test_add_type_annotations(self):
        annotations = etree_to_dict.__annotations__
        expected = {
            'e': Element,
            'return': dict
        }
        self.assertEqual(annotations, expected)

    def test_rename_parameter(self):
        parameters = inspect.signature(etree_to_dict).parameters
        self.assertIn('e', parameters)
        self.assertNotIn('t', parameters)
        
if __name__ == '__main__':
    unittest.main()

