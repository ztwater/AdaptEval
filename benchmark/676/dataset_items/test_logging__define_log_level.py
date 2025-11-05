import unittest
import logging
import inspect
import re

from ctx_logging import _define_log_level

class TestDefineLogLevel(unittest.TestCase):
    def setUp(self):
        # Clear previous custom levels to avoid conflicts in tests
        logging._levelToName = {k: v for k, v in logging._levelToName.items() if v.isupper()}
        logging._nameToLevel = {k: v for k, v in logging._nameToLevel.items() if k.isupper()}

    def tearDown(self):
        # Clear custom levels to ensure clean state for the next test
        logging._levelToName = {k: v for k, v in logging._levelToName.items() if v.isupper()}
        logging._nameToLevel = {k: v for k, v in logging._nameToLevel.items() if k.isupper()}

    def test_add_custom_logging_level(self):
        _define_log_level('CUSTOM_LEVEL_1', logging.DEBUG - 5)

        self.assertTrue(hasattr(logging, 'CUSTOM_LEVEL_1'))
        self.assertEqual(logging.CUSTOM_LEVEL_1, logging.DEBUG - 5)

        logger = logging.getLogger('test_logger')
        self.assertTrue(hasattr(logger, 'custom_level_1'))

        with self.assertLogs(logger, level='CUSTOM_LEVEL_1') as log:
            logger.custom_level_1('This is a custom message')
            self.assertIn('This is a custom message', log.output[0])

    def test_logging_to_root(self):
        _define_log_level('CUSTOM_LEVEL_2', logging.DEBUG - 6)

        with self.assertLogs(level='CUSTOM_LEVEL_2') as log:
            logging.custom_level_2('This is a custom message to root')
            self.assertIn('This is a custom message to root', log.output[0])

    def test_attribute_error_on_duplicate_level_name(self):
        _define_log_level('CUSTOM_LEVEL_4', logging.DEBUG - 8)
        with self.assertRaises(AttributeError):
            _define_log_level('CUSTOM_LEVEL_4', logging.DEBUG - 10)

    def test_attribute_error_on_duplicate_method_name(self):
        _define_log_level('CUSTOM_LEVEL_5', logging.DEBUG - 9)
        with self.assertRaises(AttributeError):
            _define_log_level('DEBUG_CUSTOM', logging.DEBUG - 10, methodName='custom_level_5')

    def test_fstring(self):
        source_code = inspect.getsource(_define_log_level)
        # Define the pattern to find f-strings (the 'f' prefix before the string)
        f_string_pattern = r'\bf"'
        # Search for the pattern in the source code
        f_string_found = re.findall(f_string_pattern, source_code)
        f_string_count = len(f_string_found)
        # Assert that an f-string was found
        self.assertEqual(f_string_count, 3, "The greet method does not use an f-string")


if __name__ == '__main__':
    unittest.main()
