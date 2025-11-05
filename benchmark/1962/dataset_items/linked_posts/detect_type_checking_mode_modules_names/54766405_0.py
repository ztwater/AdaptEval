from contextlib import contextmanager


@contextmanager
def patch(object_, attribute_name, value):
    old_value = getattr(object_, attribute_name)
    try:
        setattr(object_, attribute_name, value)
        yield
    finally:
        setattr(object_, attribute_name, old_value)
