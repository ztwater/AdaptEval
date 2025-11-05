def natural_sort(key=None, _nsre=re.compile('([0-9]+)')):
    return lambda x: [int(text) if text.isdigit() else text.casefold()
            for text in _nsre.split(key(x) if key else x)]
