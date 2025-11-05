from collections import namedtuple
State = namedtuple('State', ['name', 'capital'])

class StateDatabase:
    db = [State(*args) for args in [
       ('Alabama', 'Montgomery'),
       ('Alaska', 'Juneau'),
       # ...
    ]]
