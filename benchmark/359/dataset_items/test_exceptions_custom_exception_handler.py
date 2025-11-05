import unittest
from django.http import HttpRequest, HttpResponse
from django.conf import settings
settings.configure(DEBUG=True)
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
import re
import inspect

from exceptions import custom_exception_handler


class TestCustomExceptionHandler(unittest.TestCase):
    def setUp(self):
        # Set up a mock request and response to be used in the tests
        self.request = HttpRequest()
        self.response = HttpResponse()

    def test_custom_exception_handler_with_api_exception(self):
        # Test the custom_exception_handler with an APIException
        exc = APIException(detail='An error occurred', code='123')
        response = custom_exception_handler(exc, context={'request': self.request, 'response': self.response})

        # Check if the response is a Response object
        self.assertIsInstance(response, Response)

        # Check if the response data has the correct structure
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'An error occurred')

        # Check if the response has the correct error code
        self.assertIn('code', response.data)
        self.assertEqual(response.data['code'], '123')

    def test_custom_exception_handler_with_non_api_exception(self):
        # Test the custom_exception_handler with a non-APIException
        exc = Exception('A general exception occurred')
        response = custom_exception_handler(exc, context={'request': self.request, 'response': self.response})

        # Since it's not an APIException, the default exception_handler should be used
        self.assertIsNone(response)

    def test_insert_import_statement(self):
        source = inspect.getsource(custom_exception_handler)
        matched_import = re.search(r'from\s*rest_framework\.views\s*import\s*exception_handler|'
                                   r'import\s*rest_framework\.views\.exception_handler',
                                   source)
        self.assertIsNotNone(matched_import)

if __name__ == '__main__':
    unittest.main()