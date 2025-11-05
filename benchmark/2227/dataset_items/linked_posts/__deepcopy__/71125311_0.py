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
        
        # Bind to cp by types.MethodType
        cp.__deepcopy__ = types.MethodType(deepcopy_method.__func__, cp)

        return cp
