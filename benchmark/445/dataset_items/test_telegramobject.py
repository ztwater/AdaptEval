def all_subclasses(cls):
    # Gets all subclasses of the specified object, recursively. from
    # https://stackoverflow.com/a/3862957/9706202
    # also includes the class itself
    return (
        set(cls.__subclasses__())
        .union([s for c in cls.__subclasses__() for s in all_subclasses(c)])
        .union({cls})
    )
    # return (
    #     set(cls.__subclasses__())
    #     .union([s for c in cls.__subclasses__() for s in all_subclasses(c)])
    # )

