def __dict__(self):
    d = {
    'attr_1' : self.attr_1,
    ...
    }
    return d

# Call __dict__
d = instance.__dict__()
