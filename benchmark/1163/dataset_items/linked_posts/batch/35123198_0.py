def dict_to_object(dick):
    # http://stackoverflow.com/a/1305663/968442

    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    return Struct(**dick)
