import sys

class ProgressBar(object):
    CHAR_ON  = '='
    CHAR_OFF = ' '

    def __init__(self, end=100, length=65):
        self._end = end
        self._length = length
        self._chars = None
        self._value = 0

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = max(0, min(value, self._end))
        if self._chars != (c := int(self._length * (self._value / self._end))):
            self._chars = c
            sys.stdout.write("\r  {:3n}% [{}{}]".format(
                int((self._value / self._end) * 100.0),
                self.CHAR_ON  * int(self._chars),
                self.CHAR_OFF * int(self._length - self._chars),
            ))
            sys.stdout.flush()

    def __enter__(self):
        self.value = 0
        return self

    def __exit__(self, *args, **kwargs):
        sys.stdout.write('\n')
