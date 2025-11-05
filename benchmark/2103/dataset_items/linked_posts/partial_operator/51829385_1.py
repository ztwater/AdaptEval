def rpartial(func, *args):
    """Partially applies last arguments."""
    return lambda *a: func(*(a + args))
