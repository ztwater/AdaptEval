def foo(*args):
    return 0 if not args else max(args) - min(args)
