def instance_attributes(obj: Any) -> Dict[str, Any]:
    """Get a name-to-value dictionary of instance attributes of an arbitrary object."""
    try:
        return vars(obj)
    except TypeError:
        pass

    # object doesn't have __dict__, try with __slots__
    try:
        slots = obj.__slots__
    except AttributeError:
        # doesn't have __dict__ nor __slots__, probably a builtin like str or int
        return {}
    # collect all slots attributes (some might not be present)
    attrs = {}
    for name in slots:
        try:
            attrs[name] = getattr(obj, name)
        except AttributeError:
            continue
    return attrs
