import unittest
import logging
import inspect

from ctx_logging import add_logging_level


# Test cases
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

    def test_attribute_error_on_duplicate_level_name(self):
        add_logging_level('CUSTOM_LEVEL_4', logging.DEBUG - 8)
        with self.assertRaises(AttributeError):
            add_logging_level('CUSTOM_LEVEL_4', logging.DEBUG - 10)

    def test_update_method_name(self):
        pass

    def test_rename_parameters(self):
        parameters = inspect.signature(add_logging_level).parameters
        self.assertEqual("level_name", list(parameters.keys())[0])
        self.assertEqual("level_num", list(parameters.keys())[1])
        self.assertEqual("method_name", list(parameters.keys())[2])


if __name__ == '__main__':
    unittest.main()
