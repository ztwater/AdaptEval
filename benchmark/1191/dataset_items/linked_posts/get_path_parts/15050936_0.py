def split_path(p):
    a,b = os.path.split(p)
    return (split_path(a) if len(a) and len(b) else []) + [b]
