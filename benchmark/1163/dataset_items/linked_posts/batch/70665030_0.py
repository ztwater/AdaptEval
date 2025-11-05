class DotDict(dict):
    # https://stackoverflow.com/a/70665030/913098
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])

    Iterable are assumed to have a constructor taking list as input.
    """

    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)

        args_with_kwargs = []
        for arg in args:
            args_with_kwargs.append(arg)
        args_with_kwargs.append(kwargs)
        args = args_with_kwargs

        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v
                    if isinstance(v, dict):
                        self[k] = DotDict(v)
                    elif isinstance(v, str) or isinstance(v, bytes):
                        self[k] = v
                    elif isinstance(v, Iterable):
                        klass = type(v)
                        map_value: List[Any] = []
                        for e in v:
                            map_e = DotDict(e) if isinstance(e, dict) else e
                            map_value.append(map_e)
                        self[k] = klass(map_value)



    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(DotDict, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(DotDict, self).__delitem__(key)
        del self.__dict__[key]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__.update(d)


if __name__ == "__main__":
    import pickle
    def test_map():
        d = {
            "a": 1,
            "b": {
                "c": "d",
                "e": 2,
                "f": None
            },
            "g": [],
            "h": [1, "i"],
            "j": [1, "k", {}],
            "l":
                [
                    1,
                    "m",
                    {
                        "n": [3],
                        "o": "p",
                        "q": {
                            "r": "s",
                            "t": ["u", 5, {"v": "w"}, ],
                            "x": ("z", 1)
                        }
                    }
                ],
        }
        map_d = DotDict(d)
        w = map_d.l[2].q.t[2].v
        assert w == "w"

        pickled = pickle.dumps(map_d)
        unpickled = pickle.loads(pickled)
        assert unpickled == map_d

        kwargs_check = DotDict(a=1, b=[dict(c=2, d="3"), 5])
        assert kwargs_check.b[0].d == "3"

        kwargs_and_args_check = DotDict(d, a=1, b=[dict(c=2, d="3"), 5])
        assert kwargs_and_args_check.l[2].q.t[2].v == "w"
        assert kwargs_and_args_check.b[0].d == "3"



    test_map()

