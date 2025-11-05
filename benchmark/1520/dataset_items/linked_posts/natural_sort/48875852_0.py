def find_first_digit(s, non=False):
    for i, x in enumerate(s):
        if x.isdigit() ^ non:
            return i
    return -1

def split_digits(s, case=False):
    non = True
    while s:
        i = find_first_digit(s, non)
        if i == 0:
            non = not non
        elif i == -1:
            yield int(s) if s.isdigit() else s if case else s.lower()
            s = ''
        else:
            x, s = s[:i], s[i:]
            yield int(x) if x.isdigit() else x if case else x.lower()

def natural_key(s, *args, **kwargs):
    return tuple(split_digits(s, *args, **kwargs))
