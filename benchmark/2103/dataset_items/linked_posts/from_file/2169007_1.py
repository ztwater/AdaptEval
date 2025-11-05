def __getitem__(self, key):
    assert isinstance(key, slice)
    return String(self.__string[key], self.__simple[key])
