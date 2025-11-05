def decorator(func=None, arg=None):
    if func:
        print('success')
        return func
    else:
        print('failure')
        if arg:
            print(arg)
        return print


@decorator('i am an str')
def hello():
    print('hello')
    return


hello()
