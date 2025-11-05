# util/files.py

CHAR_MAX_LEN = 31
CHAR_REPLACE = '_'

ILLEGAL_CHARS = [
    '#',  # pound
    '%',  # percent
    '&',  # ampersand
    '{',  # left curly bracket
    '}',  # right curly bracket
    '\\',  # back slash
    '<',  # left angle bracket
    '>',  # right angle bracket
    '*',  # asterisk
    '?',  # question mark
    '/',  # forward slash
    ' ',  # blank spaces
    '$',  # dollar sign
    '!',  # exclamation point
    "'",  # single quotes
    '"',  # double quotes
    ':',  # colon
    '@',  # at sign
    '+',  # plus sign
    '`',  # backtick
    '|',  # pipe
    '=',  # equal sign
]


def generate_filename(
        name, char_replace=CHAR_REPLACE, length=CHAR_MAX_LEN, 
        illegal=ILLEGAL_CHARS, replace_dot=False):
    ''' return clean filename '''
    # init
    _elem = name.split('.')
    extension = _elem[-1].strip()
    _length = length - len(extension) - 1
    label = '.'.join(_elem[:-1]).strip()[:_length]
    filename = ''
    
    # replace '.' ?
    if replace_dot:
        label = label.replace('.', char_replace)
    
    # clean
    for char in label + '.' + extension:
        if char in illegal:
            char = char_replace
        filename += char      
    
    return filename

