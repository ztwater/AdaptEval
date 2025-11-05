>>> import string
>>> safechars = bytearray(('_-.()' + string.digits + string.ascii_letters).encode())
>>> allchars = bytearray(range(0x100))
>>> deletechars = bytearray(set(allchars) - set(safechars))
>>> filename = u'#ab\xa0c.$%.txt'
>>> safe_filename = filename.encode('ascii', 'ignore').translate(None, deletechars).decode()
>>> safe_filename
'abc..txt'
