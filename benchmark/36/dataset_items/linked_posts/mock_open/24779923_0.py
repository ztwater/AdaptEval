m = unittest.mock.MagicMock(name='open', spec=open)
m.return_value = iter(self.TEST_TEXT)

with unittest.mock.patch('builtins.open', m):
