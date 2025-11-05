class Foo(FooBase):
    def __init__(self, param1, param2):
        self._base_params = [param1, param2]
        super(Foo, result).__init__(*self._base_params)

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        super(Foo, result).__init__(*self._base_params)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        super(Foo, result).__init__(*self._base_params)
        return result
