from itertools import count

def stack_size2a(var_0=2):
    """Get stack size for caller's frame.
    """
    var_1 = sys._getframe(var_0)

    for var_0 in count(var_0):
        var_1 = var_1.f_back
        if not var_1:
            return var_0
