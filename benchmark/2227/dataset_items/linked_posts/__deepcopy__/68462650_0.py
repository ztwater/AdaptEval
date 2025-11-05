from copy import deepcopy
import types


class Good:
    def __init__(self):
        self.i = 0

    def __deepcopy__(self, memo):
        deepcopy_method = self.__deepcopy__
        self.__deepcopy__ = None
        cp = deepcopy(self, memo)
        self.__deepcopy__ = deepcopy_method
        # Copy the function object
        func = types.FunctionType(
            deepcopy_method.__code__,
            deepcopy_method.__globals__,
            deepcopy_method.__name__,
            deepcopy_method.__defaults__,
            deepcopy_method.__closure__,
        )
        # Bind to cp and set
        bound_method = func.__get__(cp, cp.__class__)
        cp.__deepcopy__ = bound_method

        return cp


class Bad:
    def __init__(self):
        self.i = 0

    def __deepcopy__(self, memo):
        deepcopy_method = self.__deepcopy__
        self.__deepcopy__ = None
        cp = deepcopy(self, memo)
        self.__deepcopy__ = deepcopy_method
        cp.__deepcopy__ = deepcopy_method
        return cp


x = Bad()
copy = deepcopy(x)
copy.i = 1
copy_of_copy = deepcopy(copy)
print(copy_of_copy.i)  # 0

x = Good()
copy = deepcopy(x)
copy.i = 1
copy_of_copy = deepcopy(copy)
print(copy_of_copy.i)  # 1
