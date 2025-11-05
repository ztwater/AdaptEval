>>> import string
>>> valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
>>> valid_chars
'-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
>>> filename = "This Is a (valid) - filename%$&$ .txt"
>>> ''.join(c for c in filename if c in valid_chars)
'This Is a (valid) - filename .txt'
