import inspect
import unittest
from collections import OrderedDict
from unittest.mock import patch
import yaml

from ctx_utils import yaml_ordered_load

class TestYamlOrderedLoad(unittest.TestCase):
    def test_function_rename(self):
        import ctx_utils
        self.assertTrue(callable(yaml_ordered_load))
        self.assertFalse('ordered_load' in ctx_utils.__dict__)
    
    def test_default_loader(self):
        parameters = inspect.signature(yaml_ordered_load).parameters
        self.assertEqual(parameters['Loader'].default, yaml.Loader)
        self.assertNotEqual(parameters['Loader'].default, yaml.SafeLoader)

    def test_empty_yaml(self):
        yaml_content = ""
        stream = yaml_content
        result = yaml_ordered_load(stream)
        expected = None  # OrderedDict()
        self.assertEqual(result, expected)

    def test_nested_yaml(self):
        yaml_content = """
        a:
          b: 2
          c: 3
        """
        stream = yaml_content
        result = yaml_ordered_load(stream)
        expected = OrderedDict([('a', OrderedDict([('b', 2), ('c', 3)]))])
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()