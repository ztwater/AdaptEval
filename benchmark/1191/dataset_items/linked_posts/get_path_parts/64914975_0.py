def parts(path):
    p,f = os.path.split(os.path.normpath(path))
    return parts(p) + [f] if f and p else [p] if p else []
