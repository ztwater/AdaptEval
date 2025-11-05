def natural_sort(l, attrib):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key.__dict__[attrib])]
    return sorted(l, key=alphanum_key)

results = natural_sort(albums, 'albumid')
