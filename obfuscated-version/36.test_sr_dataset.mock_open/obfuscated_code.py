def mock_open(*var_0, **var_1):
  var_2 = unittest.mock.mock_open(*var_0, **var_1)
  var_2.return_value.__iter__ = lambda self : iter(self.readline, '')
  return var_2
