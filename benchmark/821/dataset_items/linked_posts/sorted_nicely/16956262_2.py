def keyfunc(s):
    return [int(''.join(g)) if k else ''.join(g) for k, g in groupby('\0'+s, str.isdigit)]
