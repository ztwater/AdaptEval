class decorator_with_arguments(object):

    def __new__(cls, decorated_function=None, **kwargs):

        self = super().__new__(cls)
        self._init(**kwargs)

        if not decorated_function:
            return self
        else:
            return self.__call__(decorated_function)

    def _init(self, arg1="default", arg2="default", arg3="default"):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, decorated_function):

        def wrapped_f(*args):
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            print("decorated_function arguments:", *args)
            decorated_function(*args)

        return wrapped_f

@decorator_with_arguments(arg1=5)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

@decorator_with_arguments()
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

@decorator_with_arguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)
