from collections import namedtuple
class StateDatabase:
    State = namedtuple('State', ['name', 'capital'])
    db = [State(*args) for State in [State] for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]
