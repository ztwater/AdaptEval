def camel_case_split(string):
    bldrs = [[string[0].upper()]]
    for c in string[1:]:
        if bldrs[-1][-1].islower() and c.isupper():
            bldrs.append([c])
        else:
            bldrs[-1].append(c)
    return [''.join(bldr) for bldr in bldrs]
