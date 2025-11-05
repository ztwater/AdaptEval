class Foo:
    def __init__(self):
        # keys are initialized with
        # their respective values
        self.bar = 'hello'
        self.baz = 'world'
  
f = Foo()
print (f.__dict__) # {'bar': 'hello', 'baz': 'world'}

