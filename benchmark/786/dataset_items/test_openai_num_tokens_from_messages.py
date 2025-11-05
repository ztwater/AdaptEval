import unittest
from openai import OpenAIWrapper
from unittest.mock import MagicMock, patch

class TestNumTokensFromMessages(unittest.TestCase):

    def setUp(self):
        self.openai_wrapper = OpenAIWrapper(None, None)

    def test_instance_method_signature(self):
        # Test that the method signature has been changed to an instance method.
        self.assertTrue(hasattr(self.openai_wrapper, 'num_tokens_from_messages'))
        self.assertIn('self', OpenAIWrapper.num_tokens_from_messages.__code__.co_varnames)

    def test_num_tokens_from_messages_list(self):
        # Test with a list of messages
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what's the weather like?"}
        ]
        expected_tokens = 27
        self.assertEqual(
            self.openai_wrapper.num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"),
            expected_tokens
        )
    
    def test_num_tokens_from_messages_str(self):
        # Test with a string message
        message = "Hello, how are you?"
        expected_tokens = 6
        self.assertEqual(
            self.openai_wrapper.num_tokens_from_messages(message, model="gpt-3.5-turbo-0301"),
            expected_tokens
        )
    
    def test_num_tokens_from_messages_with_name(self):
        # Test with a message that includes a name
        messages = [
            {"role": "system", "name": "Assistant", "content": "I am an AI."}
        ]
        expected_tokens = 13
        self.assertEqual(
            self.openai_wrapper.num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"),
            expected_tokens
        )

    def test_num_tokens_from_messages_with_gpt_3_5_turbo(self):
        # Test with gpt-3.5-turbo model
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what's the weather like?"}
        ]
        expected_tokens = 27
        self.assertEqual(
            self.openai_wrapper.num_tokens_from_messages(messages, model="gpt-3.5-turbo"),
            expected_tokens
        )
    
    def test_num_tokens_from_messages_with_gpt_4(self):
        # Test with gpt-4 model
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what's the weather like?"}
        ]
        expected_tokens = 25
        self.assertEqual(
            self.openai_wrapper.num_tokens_from_messages(messages, model="gpt-4"),
            expected_tokens
        )
    
    def test_num_tokens_from_messages_with_gpt_4_0314(self):
        # Test with gpt-4 model
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what's the weather like?"}
        ]
        expected_tokens = 25
        self.assertEqual(
            self.openai_wrapper.num_tokens_from_messages(messages, model="gpt-4-0314"),
            expected_tokens
        )

    
    def test_num_tokens_from_messages_with_unknown_model(self):
        # Test with an unknown model
        with self.assertRaises(NotImplementedError):
            self.openai_wrapper.num_tokens_from_messages([], model="unknown_model")

    @patch('openai.tiktoken.encoding_for_model')
    @patch('openai.tiktoken.get_encoding')
    def test_num_tokens_from_messages_key_error(self, mock_get_encoding, mock_encoding_for_model):
        # Simulate a KeyError for an unrecognized model
        mock_encoding_for_model.side_effect = KeyError("Model not found")

        with self.assertRaises(NotImplementedError):
            num_tokens = self.openai_wrapper.num_tokens_from_messages([], model="unrecognized_model")
        mock_get_encoding.assert_called_with("cl100k_base")


if __name__ == '__main__':
    unittest.main()
