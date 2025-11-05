def stripEscape(string):
    """ Removes all escape sequences from the input string """
    delete = ""
    i=1
    while (i<0x20):
        delete += chr(i)
        i += 1
    t = string.translate(None, delete)
    return t
