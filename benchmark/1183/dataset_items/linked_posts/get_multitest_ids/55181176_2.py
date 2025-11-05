from collections import namedtuple
import itertools as it

class StateDatabase:
    State = namedtuple('State', ['name', 'capital'])
    db = [State(*args) for State, args in zip(it.repeat(State), [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ])]
