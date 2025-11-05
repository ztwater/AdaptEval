def mock_open(*args, **kargs):
  f_open = unittest.mock.mock_open(*args, **kargs)
  f_open.return_value.__iter__ = lambda self : iter(self.readline, '')
  return f_open
