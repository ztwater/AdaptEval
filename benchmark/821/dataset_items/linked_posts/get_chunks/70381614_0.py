class ChunksIterator(object):
    def __init__(self, data, n):
        self._data = data
        self._l = len(data)
        self._n = n

    def __iter__(self):
        for i in range(0, self._l, self._n):
            yield self._data[i:i + self._n]

    def __len__(self):
        rem = 1 if self._l % self._n != 0 else 0
        return self._l // self._n + rem
