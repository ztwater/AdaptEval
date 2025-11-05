def camel_case_split(s):
    idx = list(map(str.isupper, s))
    # mark change of case
    l = [0]
    for (i, (x, y)) in enumerate(zip(idx, idx[1:])):
        if x and not y:  # "Ul"
            l.append(i)
        elif not x and y:  # "lU"
            l.append(i+1)
    l.append(len(s))
    # for "lUl", index of "U" will pop twice, have to filter that
    return [s[x:y] for x, y in zip(l, l[1:]) if x < y]
