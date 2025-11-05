import unittest
from read_action_classes import read_label_map

class TestReadLabelMap(unittest.TestCase):
    def setUp(self):
        self.valid_label_map_content = """item {
            id: 1
            name: 'person'
        }
        item {
            id: 2
            name: 'bicycle'
        }"""
        
        self.invalid_id_label_map_content = """item {
            id: 'abc'
            name: 'person'
        }"""
        
        self.label_map_file = "label_map.pbtxt"

    def create_label_map_file(self, content):
        with open(self.label_map_file, 'w') as f:
            f.write(content)

    def test_read_label_map_valid(self):
        self.create_label_map_file(self.valid_label_map_content)
        result = read_label_map(self.label_map_file)
        expected = {'person': 1, 'bicycle': 2}
        self.assertEqual(result, expected)
    
    def test_read_label_map_id_parsing_exception(self):
        self.create_label_map_file(self.invalid_id_label_map_content)
        with self.assertRaises(Exception):
            read_label_map(self.label_map_file)
    
    def test_read_label_map_remove_double_quotes(self):
        content = """item {
            id: 1
            name: "person"
        }"""
        self.create_label_map_file(content)
        result = read_label_map(self.label_map_file)
        expected = {'"person"': 1}
        self.assertEqual(result, expected)
    
    def tearDown(self):
        import os
        os.remove(self.label_map_file)


if __name__ == '__main__':
    unittest.main()
