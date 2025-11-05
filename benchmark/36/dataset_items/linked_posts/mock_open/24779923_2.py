# Python 2!
m = mock.mock_open(read_data=''.join(self.TEST_TEXT))
m.return_value.__iter__ = lambda self: iter(self.readline, '')
