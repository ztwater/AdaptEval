def __init__(self, string, simple = None):
    if simple is None:
        self.__string = tuple(string.split())
        self.__simple = tuple(self.__simple())
    else:
        self.__string = string
        self.__simple = simple
