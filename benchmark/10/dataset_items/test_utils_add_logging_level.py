import inspect
import logging
import re
import unittest
from typing import Optional

from ctx_utils import add_logging_level

class TestAddLoggingLevel(unittest.TestCase):

    def setUp(self):
        # Clear previous custom levels to avoid conflicts in tests
        logging._levelToName = {k: v for k, v in logging._levelToName.items() if v.isupper()}
        logging._nameToLevel = {k: v for k, v in logging._nameToLevel.items() if k.isupper()}

    def tearDown(self):
        # Clear custom levels to ensure clean state for the next test
        logging._levelToName = {k: v for k, v in logging._levelToName.items() if v.isupper()}
        logging._nameToLevel = {k: v for k, v in logging._nameToLevel.items() if k.isupper()}

    def test_add_custom_logging_level(self):
        add_logging_level('CUSTOM_LEVEL_1', logging.DEBUG - 5)

        self.assertTrue(hasattr(logging, 'CUSTOM_LEVEL_1'))
        self.assertEqual(logging.CUSTOM_LEVEL_1, logging.DEBUG - 5)

        logger = logging.getLogger('test_logger')
        self.assertTrue(hasattr(logger, 'custom_level_1'))

        with self.assertLogs(logger, level='CUSTOM_LEVEL_1') as log:
            logger.custom_level_1('This is a custom message')
            self.assertIn('This is a custom message', log.output[0])

    def test_logging_to_root(self):
        add_logging_level('CUSTOM_LEVEL_2', logging.DEBUG - 6)

        with self.assertLogs(level='CUSTOM_LEVEL_2') as log:
            logging.custom_level_2('This is a custom message to root')
            self.assertIn('This is a custom message to root', log.output[0])

    def test_logging_with_logger_adapter(self):
        add_logging_level('CUSTOM_LEVEL_3', logging.DEBUG - 7)

        logger = logging.getLogger('test_logger')
        adapter = logging.LoggerAdapter(logger, {})

        self.assertTrue(hasattr(adapter, 'custom_level_3'))

        with self.assertLogs(logger, level='CUSTOM_LEVEL_3') as log:
            adapter.custom_level_3('This is a custom message from adapter')
            self.assertIn('This is a custom message from adapter', log.output[0])

    def test_attribute_error_on_duplicate_level_name(self):
        add_logging_level('CUSTOM_LEVEL_4', logging.DEBUG - 8)
        with self.assertRaises(AttributeError):
            add_logging_level('CUSTOM_LEVEL_4', logging.DEBUG - 10)

    def test_attribute_error_on_duplicate_method_name(self):
        add_logging_level('CUSTOM_LEVEL_5', logging.DEBUG - 9)
        with self.assertRaises(AttributeError):
            add_logging_level('DEBUG_CUSTOM', logging.DEBUG - 10, methodName='custom_level_5')

    def test_rename_function(self):
        add_logging_level('CUSTOM_LEVEL_0', logging.DEBUG - 5)

    def test_add_type_annotations(self):
        annotations = add_logging_level.__annotations__
        expected = {
            'levelName': str,
            'levelNum': int,
            'methodName': Optional[str],
            'return': None
        }
        self.assertEqual(annotations, expected)

    def test_add_method_for_logger_adapter(self):
        source = inspect.getsource(add_logging_level)
        matched_method = re.search(r'def\s+adapterLog\(', source)
        self.assertIsNotNone(matched_method)

if __name__ == '__main__':
    unittest.main()

