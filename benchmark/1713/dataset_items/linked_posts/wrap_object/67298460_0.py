import contextlib

class Patcher:
    UNCHANGED_RET = object()

    def __init__(self):
        self.call_count = 0
        self.return_value = Patcher.UNCHANGED_RET


@contextlib.contextmanager
def patch(klass, method_name):
    patcher = Patcher()
    orig_method = getattr(klass, method_name)

    def new_method(myself, *args, **kwargs):
        patcher.call_count += 1
        orig_return_value = orig_method(myself, *args, **kwargs)

        if patcher.return_value != Patcher.UNCHANGED_RET:
            return patcher.return_value

        return orig_return_value

    setattr(klass, method_name, new_method)
    yield patcher
    setattr(klass, method_name, orig_method)
