reduce(lambda x, y: x + tuple(i for i in y if i is not None), zip_longest(*data))
