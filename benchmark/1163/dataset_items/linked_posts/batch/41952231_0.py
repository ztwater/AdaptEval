payload = {
    "name": "John",
    "location": {
        "lat": 53.12312312,
        "long": 43.21345112
    },
    "numbers": [
        {
            "role": "home",
            "number": "070-12345678"
        },
        {
            "role": "office",
            "number": "070-12345679"
        }
    ]
}


class Map(object):
    """
    Dot style access to object members, access raw values
    with an underscore e.g.

    class Foo(Map):
        def foo(self):
            return self.get('foo') + 'bar'

    obj = Foo(**{'foo': 'foo'})

    obj.foo => 'foobar'
    obj._foo => 'foo'

    """

    def __init__(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self.__dict__[k] = v
                    self.__dict__['_' + k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self.__dict__[k] = v
                self.__dict__['_' + k] = v

    def __getattribute__(self, attr):
        if hasattr(self, 'get_' + attr):
            return object.__getattribute__(self, 'get_' + attr)()
        else:
            return object.__getattribute__(self, attr)

    def get(self, key):
        try:
            return self.__dict__.get('get_' + key)()
        except (AttributeError, TypeError):
            return self.__dict__.get(key)

    def __repr__(self):
        return u"<{name} object>".format(
            name=self.__class__.__name__
        )


class Number(Map):
    def get_role(self):
        return self.get('role')

    def get_number(self):
        return self.get('number')


class Location(Map):
    def get_latitude(self):
        return self.get('lat') + 1

    def get_longitude(self):
        return self.get('long') + 1


class Item(Map):
    def get_name(self):
        return self.get('name') + " Doe"

    def get_location(self):
        return Location(**self.get('location'))

    def get_numbers(self):
        return [Number(**n) for n in self.get('numbers')]


# Tests

obj = Item({'foo': 'bar'}, **payload)

assert type(obj) == Item
assert obj._name == "John"
assert obj.name == "John Doe"
assert type(obj.location) == Location
assert obj.location._lat == 53.12312312
assert obj.location._long == 43.21345112
assert obj.location.latitude == 54.12312312
assert obj.location.longitude == 44.21345112

for n in obj.numbers:
    assert type(n) == Number
    if n.role == 'home':
        assert n.number == "070-12345678"
    if n.role == 'office':
        assert n.number == "070-12345679"
