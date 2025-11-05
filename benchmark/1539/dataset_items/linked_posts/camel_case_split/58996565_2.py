def camel_case_split(s):
    u = True  # case of previous char
    w = b = ''  # current word, buffer for last uppercase letter
    for c in s:
        o = c.isupper()
        if u and o:
            w += b
            b = c
        elif u and not o:
            if len(w)>0:
                yield w
            w = b + c
            b = ''
        elif not u and o:
            yield w
            w = ''
            b = c
        else:  # not u and not o:
            w += c
        u = o
    if len(w)>0 or len(b)>0:  # flush
        yield w + b
