f_open = unittest.mock.mock_open(read_data='foo\nbar\n')
f = f_open('blah')
for line in f:
  print(line)
