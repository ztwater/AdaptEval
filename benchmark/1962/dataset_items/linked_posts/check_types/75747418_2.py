def evaluate_type(name: str):
    t = globals().get(name)
    if t:
        return t
    else:
        try:
            t = getattr(__builtins__, name)
            if isinstance(t, type):
                return t
            else:
                raise ValueError(name)
        except:
            raise ValueError(name)


evaluate_type("int")

evaluate_type("Hey")
