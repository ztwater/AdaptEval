def foo(*args):
    if not len(args):
        return 0
    
    return max(args) - min(args)
