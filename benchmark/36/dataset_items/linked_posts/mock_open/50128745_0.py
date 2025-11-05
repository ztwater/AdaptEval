text_file_data = '\n'.join(["a line here", "the second line", "another 
line in the file"])
with patch('__builtin__.open', mock_open(read_data=text_file_data), 
create=True) as m:
    # mock_open doesn't properly handle iterating over the open file with for line in file:
    # but if we set the return value like this, it works.
    m.return_value.__iter__.return_value = text_file_data.splitlines()
    with open('filename', 'rU') as f:
        for line in f:
            print line
