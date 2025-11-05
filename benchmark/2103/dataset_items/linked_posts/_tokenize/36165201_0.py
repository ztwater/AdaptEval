def tokenize(line, separator=',', whitespace="\t\n\x20", quote='"'):
    """
    >>> tokenize('"some string" 10.0, 5')
    ['some string', '10.0', '5']

    >>> tokenize(' "other string", 15.0 /')
    ['other string', '15.0', '/']

    >>> tokenize('"nother string", , 7')
    ['nother string', '', '7']

    """
    inside_str = False
    token_started = False
    token = ""
    tokens = []
    separated = False
    just_added = False
    for char in line:
        if char in quote:
            if not inside_str:
                inside_str = True

            else:
                inside_str = False
                tokens.append(token)
                token = ""
                just_added = True
            continue
        if char in (whitespace + separator) and not inside_str:
            if token:
                tokens.append(token)
                token = ""
                just_added = True
            elif char in separator:
                if not just_added:
                    tokens.append("")
                just_added = False
            continue
        token += char
    if token:
        tokens.append(token)
    return tokens


class Character(object):
    def __init__(self, length=None):
        self.length = length
    def __call__(self, text):
        if self.length is None:
            return text
        if len(text) > self.length:
            return text[:self.length]
        return "{{:{}}}".format(self.length).format(text)


def make_types(types, default_value):
    return types, [default_value] * len[types]


def fortran_reader(file, types, default_char="/", default_value=None, **kw):
    types, results = make_types(types, default_value)
    tokens = []
    while True:
        tokens = []
        while len(tokens) < len(results):
            try:
                line = next(file)
            except StopIteration:
                raise StopIteration
            tokens += tokenize(line, **kw)
        for i, (type_, token) in enumerate(zip(types, tokens)):
            if not token or token in default_char:
                continue
            results[i] = type_(token)
        changed_types = yield(results)
        if changed_types:
            types, results = make_types(changed_types)
