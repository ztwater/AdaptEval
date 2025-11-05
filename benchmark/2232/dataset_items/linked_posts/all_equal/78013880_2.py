class EqualPairwiseIterator():

    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.previous_value = None
        if len(iterable) < 1:
            raise ValueError(f'EqualPairwiseIterator does not work with lists of length 0')

    def __iter__(self):
        try:
            self.previous_value = next(self.iterator) # will raise StopException when out of range
        except StopException as stop_exception:
            raise ValueError(f'EqualPairwiseIterator does not work with lists of length 0')
        return self

    def __next__(self):
        
        next_value = next(self.iterator) # will raise StopException when out of range
        op_value = operator.eq(next_value, self.previous_value)
        self.previous_value = next_value
        return op_value 

# useage:
iterable = [...]
all(EqualPairwiseIterator(iterable))
