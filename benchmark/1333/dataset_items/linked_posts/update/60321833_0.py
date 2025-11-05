def deepupdate(original, update):
    """Recursively update a dict.

    Subdict's won't be overwritten but also updated.
    """
    if not isinstance(original, abc.Mapping):
        return update
    for key, value in update.items():
        if isinstance(value, abc.Mapping):
            original[key] = deepupdate(original.get(key, {}), value)
        else:
            original[key] = value
    return original
