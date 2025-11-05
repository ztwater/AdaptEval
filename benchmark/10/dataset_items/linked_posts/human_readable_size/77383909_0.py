class Unit(int):
    multiplier = 1000
    precision = 2
    prefixes = ('', 'k')
    unit = '?'

    def __str__(self):
        number = self
        for prefix in self.prefixes:
            if number < self.multiplier or prefix == self.prefixes[-1]:
                break
            number /= float(self.multiplier)
        if prefix:
            return f'{number:.{self.precision}f}{prefix}{self.unit}'
        return f'{int(number)}{self.unit}'


class Filesize(Unit):
    multiplier = 1024
    prefixes = ('', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi')
    unit = 'B'

class Distance(Unit):
    unit = 'm'


# Prints 123m
print(Distance(123))

# Prints 123456.8km
print(Distance(123456789))
