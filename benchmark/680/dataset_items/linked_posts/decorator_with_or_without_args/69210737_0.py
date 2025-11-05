def redirect_output(func=None, /, *, output_log='./output.log'):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            print(f"{func.__name__} finished, output_log:{output_log}")
            return res

        return wrapper

    if func is None:
        return out_wrapper  # @redirect_output()
    return out_wrapper(func)  # @redirect_output


@redirect_output
def test1():
    print("running test 1")


@redirect_output(output_log="new.log")
def test2():
    print("running test 2")

test1()
print('-----')
test2()
