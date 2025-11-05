from itertools import count

def stack_size3a(size=2):
    """Get stack size for caller's frame.
    """
    frame = sys._getframe(size)
    try:
        for size in count(size, 8):
            frame = frame.f_back.f_back.f_back.f_back.\
                f_back.f_back.f_back.f_back
    except AttributeError:
        while frame:
            frame = frame.f_back
            size += 1
        return size - 1
