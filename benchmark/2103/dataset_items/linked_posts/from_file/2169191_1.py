@classmethod 
def makeit(cls):
    self = cls.__new__(cls)
    # etc etc, then
    return self
