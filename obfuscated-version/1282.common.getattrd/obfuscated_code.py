class NoDefaultProvided(object):
    pass

def getattrd(var_0, var_1, var_2=NoDefaultProvided):
    """
    Same as getattr(), but allows dot notation lookup
    Discussed in:
    http://stackoverflow.com/questions/11975781
    """

    try:
        return reduce(getattr, var_1.split("."), var_0)
    except AttributeError, e:
        if var_2 != NoDefaultProvided:
            return var_2
        raise
