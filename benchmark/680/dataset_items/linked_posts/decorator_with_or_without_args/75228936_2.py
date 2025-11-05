def decorator(func=None):
    if func:
        print('success')
        return func
    else:
        print('failure')
        return print


@decorator()
def hello():
    print('hello')
    return


hello()
