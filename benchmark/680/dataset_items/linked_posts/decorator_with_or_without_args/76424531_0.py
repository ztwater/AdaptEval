from functools import partial, wraps
from inspect import signature
from typing import Callable


def decorator_with_kwargs(decorator: Callable) -> Callable:
    """Decorator factory to give decorated decorators the skill to receive
    optional keyword arguments.

    If a decorator "some_decorator" is decorated with this function:

        @decorator_with_kwargs
        def some_decorator(decorated_function, kwarg1=1, kwarg2=2):
            def wrapper(*decorated_function_args, **decorated_function_kwargs):
                '''Modifies the behavior of decorated_function according
                to the value of kwarg1 and kwarg2'''
                ...
            return wrapper

    It will be usable in the following ways:

        @some_decorator
        def func(x):
            ...

        @some_decorator()
        def func(x):
            ...

        @some_decorator(kwarg1=3)  # or other combinations of kwargs
        def func(x, y):
            ...

    :param decorator: decorator to be given optional kwargs-handling skills
    :type decorator: Callable
    :raises TypeError: if the decorator does not receive a single Callable or
        keyword arguments
    :raises TypeError: if the signature of the decorated decorator does not
        conform to: Callable, **keyword_arguments
    :return: modified decorator
    :rtype: Callable
    """
    @wraps(decorator)
    def decorator_wrapper(*args, **kwargs):
        if (len(kwargs) == 0) and (len(args) == 1) and callable(args[0]):
            return decorator(args[0])
        if len(args) == 0:
            return partial(decorator, **kwargs)
        raise TypeError(
            f'{decorator.__name__} expects either a single Callable '
            'or keyword arguments'
        )

    signature_values = signature(decorator).parameters.values()
    signature_args = [
        param.name for param in signature_values
        if param.default == param.empty
    ]

    if len(signature_args) != 1:
        raise TypeError(
            f'{decorator.__name__} signature should be of the form:\n'
            f'{decorator.__name__}(function: typing.Callable, '
            'kwarg_1=default_1, kwarg_2=default_2, ...) -> Callable'
        )

    return decorator_wrapper


# EXAMPLE USE CASES:

@decorator_with_kwargs
def multiple_runs(function, num_times=2):
    @wraps(function)
    def wrapper(*args, **kwargs):
        for _ in range(num_times):
            function(*args, **kwargs)
    return wrapper


# Decorator factory not being called directly
@multiple_runs
def func(x):
    print(x, end='')
func('a')
# > aa


# Decorator factory called without arguments
@multiple_runs()
def func(x):
    print(x, end='')
func('a')
# > aa


# Decorator factory called with keyword arguments
@multiple_runs(num_times=5)
def func(x):
    print(x, end='')
func('a')
# > aaaaa


# Expect TypeError:
# unexpected keyword argument
@multiple_runs(xpto=1)
def func(x):
    print(x, end='')
func('a')
# > TypeError: multiple_runs() got an unexpected keyword argument 'xpto'


# Expect TypeError:
# passing a non callable positional argument for the decorator:
@multiple_runs(1)
def func(x):
    print(x, end='')
func('a')
# > TypeError: multiple_runs expects either a single Callable or keyword arguments


# Expect TyeError:
# passing two positional arguments for the decorator:
@multiple_runs(1, 2)
def func(x):
    print(x, end='')   
func('a')
# > TypeError: multiple_runs expects either a single Callable or keyword arguments


# Expect TyeError:
# no workaround for something like this:
@multiple_runs(lambda x: x)
def func(x):
    print(x, end='')    
func('a')
# > TypeError: 'NoneType' object is not callable


# Expect TyeError:
# decorator with incorrect signature
@decorator_with_kwargs
def decorator_with_incorrect_signature(function, other_arg, x=1):
    pass
# > TypeError: decorator_with_incorrect_signature signature should be of the form:
# > decorator_with_incorrect_signature(function: typing.Callable, kwarg_1=default_1, kwarg_2=default_2, ...) -> Callable
