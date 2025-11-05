def max3bytes(unicode_string):
    return u''.join(uc if uc <= u'\uffff' else u'\ufffd' for uc in unicode_string)
