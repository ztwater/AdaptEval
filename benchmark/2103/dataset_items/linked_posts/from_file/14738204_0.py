>>> class MetaInit(type):

    def __call__(cls, *args, **kwargs):
        if args or kwargs:
            return super().__call__(*args, **kwargs)
        return cls.__new__(cls)

>>> class String(metaclass=MetaInit):

    def __init__(self, string):
        self.__string = tuple(string.split())
        self.__simple = tuple(self.__simple())

    def __simple(self):
        letter = lambda s: ''.join(filter(lambda s: 'a' <= s <= 'z', s))
        return filter(bool, map(letter, map(str.lower, self.__string)))

    def __eq__(self, other):
        assert isinstance(other, String)
        return self.__simple == other.__simple

    def __getitem__(self, key):
        assert isinstance(key, slice)
        string = String()
        string.__string = self.__string[key]
        string.__simple = self.__simple[key]
        return string

    def __iter__(self):
        return iter(self.__string)

>>> String('Hello, world!')[1:]
<__main__.String object at 0x02E78830>
>>> _._String__string, _._String__simple
(('world!',), ('world',))
>>> 
