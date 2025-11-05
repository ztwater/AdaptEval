>>> s = '\x1b[93;m\x1b[40;m\x1b[22;m\nFoo, spam and eggs.\x1b[0m\n'
>>> ''.join(strip_ansi_colour(s))

'\nFoo, spam and eggs.\n'
