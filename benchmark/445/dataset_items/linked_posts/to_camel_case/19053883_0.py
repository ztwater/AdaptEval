import string

def to_camel_case(s):
    return s[0].lower() + string.capwords(s, sep='_').replace('_', '')[1:] if s else s
