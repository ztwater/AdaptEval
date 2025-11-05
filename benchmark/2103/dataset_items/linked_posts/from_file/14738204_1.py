#! /usr/bin/env python3
METHOD = 'metaclass'


class NoInitMeta(type):
    def new(cls):
        return cls.__new__(cls)


class String(metaclass=NoInitMeta if METHOD == 'metaclass' else type):
    def __init__(self, value):
        self.__value = tuple(value.split())
        self.__alpha = tuple(filter(None, (
            ''.join(c for c in word.casefold() if 'a' <= c <= 'z') for word in
            self.__value)))

    def __str__(self):
        return ' '.join(self.__value)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__alpha == other.__alpha

    if METHOD == 'metaclass':
        def __getitem__(self, key):
            if not isinstance(key, slice):
                raise NotImplementedError
            instance = type(self).new()
            instance.__value = self.__value[key]
            instance.__alpha = self.__alpha[key]
            return instance
    elif METHOD == 'classmethod':
        def __getitem__(self, key):
            if not isinstance(key, slice):
                raise NotImplementedError
            instance = self.new()
            instance.__value = self.__value[key]
            instance.__alpha = self.__alpha[key]
            return instance

        @classmethod
        def new(cls):
            return cls.__new__(cls)
    elif METHOD == 'inline':
        def __getitem__(self, key):
            if not isinstance(key, slice):
                raise NotImplementedError
            cls = type(self)
            instance = cls.__new__(cls)
            instance.__value = self.__value[key]
            instance.__alpha = self.__alpha[key]
            return instance
    else:
        raise ValueError('METHOD did not have an appropriate value')

    def __iter__(self):
        return iter(self.__value)


def main():
    x = String('Hello, world!')
    y = x[1:]
    print(y)


if __name__ == '__main__':
    main()
