def uncamelize(s):
    buff, l = '', []
    for ltr in s:
        if ltr.isupper():
            if buff:
                l.append(buff)
                buff = ''
        buff += ltr
    l.append(buff)
    return '_'.join(l).lower()
