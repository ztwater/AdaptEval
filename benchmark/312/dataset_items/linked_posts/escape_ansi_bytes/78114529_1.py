>>> s = 'ls\r\n\x1b[00m\x1b[01;31mexamplefile.zip\x1b[00m\r\n\x1b[01;31m'
>>> ''.join(strip_ansi_colour(s))[2:].strip()  # Trim ls and newlines

'examplefile.zip'
