# Note: read_data must be a string!
m = unittest.mock.mock_open(read_data=''.join(self.TEST_TEXT))
m.return_value.__iter__ = lambda self: self
m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
