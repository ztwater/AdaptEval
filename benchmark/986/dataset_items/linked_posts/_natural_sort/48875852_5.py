def int_maybe(x):
    return int(x) if str(x).isdigit() else x

def split_digits_re(s, case=False):
    parts = re.findall('\d+|\D+', s)
    if not case:
        return map(int_maybe, (x.lower() for x in parts))
    else:
        return map(int_maybe, parts)
    
def natural_key_re(s, *args, **kwargs):
    return tuple(split_digits_re(s, *args, **kwargs))
