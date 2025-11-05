global_var = 'foo'

def my_function():
    print(global_var)

global_var = 'bar'
my_function()
