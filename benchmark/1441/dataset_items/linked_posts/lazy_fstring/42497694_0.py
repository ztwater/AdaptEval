import inspect

class magic_fstring_function:
    def __init__(self, payload):
        self.payload = payload
    def __str__(self):
        vars = inspect.currentframe().f_back.f_globals.copy()
        vars.update(inspect.currentframe().f_back.f_locals)
        return self.payload.format(**vars)

template = "The current name is {name}"

template_a = magic_fstring_function(template)

# use it inside a function to demonstrate it gets the scoping right
def new_scope():
    names = ["foo", "bar"]
    for name in names:
        print(template_a)

new_scope()
# The current name is foo
# The current name is bar
