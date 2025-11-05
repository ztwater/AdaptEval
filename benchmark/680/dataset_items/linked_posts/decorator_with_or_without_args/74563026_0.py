from numbers import Number

def multiply(num):
    def _multiply(func):
        def core(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(num, Number):
                return result * num
            else:
                return result
        return core
    if callable(num):
        return _multiply(num)
    else:
        return _multiply

def sum(num1, num2):
    return num1 + num2
