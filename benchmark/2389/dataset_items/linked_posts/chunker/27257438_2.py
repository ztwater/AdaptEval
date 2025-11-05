def chunker(data, size, reductor=tuple):
    return custom_zip(*[iter(data)]*size, reductor=reductor)
