from functools import WRAPPER_ASSIGNMENTS


def class_wraps(cls):
    """Update a wrapper class `cls` to look like the wrapped."""

    class Wrapper(cls):
        """New wrapper that will extend the wrapper `cls` to make it look like `wrapped`.

        wrapped: Original function or class that is beign decorated.
        assigned: A list of attribute to assign to the the wrapper, by default they are:
             ['__doc__', '__name__', '__module__', '__annotations__'].

        """

        def __init__(self, wrapped, assigned=WRAPPER_ASSIGNMENTS):
            self.__wrapped = wrapped
            for attr in assigned:
                setattr(self, attr, getattr(wrapped, attr))

            super().__init__(wrapped)

        def __repr__(self):
            return repr(self.__wrapped)

    return Wrapper
