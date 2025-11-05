def deep_get(d: dict, *keys, default=None):
    """ Safely get a nested value from a dict

    Example:
        config = {'device': None}
        deep_get(config, 'device', 'settings', 'light')
        # -> None
        
    Example:
        config = {'device': True}
        deep_get(config, 'device', 'settings', 'light')
        # -> TypeError

    Example:
        config = {'device': {'settings': {'light': 'bright'}}}
        deep_get(config, 'device', 'settings', 'light')
        # -> 'light'

    Note that it returns `default` is a key is missing or when it's None.
    It will raise a TypeError if a value is anything else but a dict or None.
    
    Args:
        d: The dict to descend into
        keys: A sequence of keys to follow
        default: Custom default value
    """
    # Descend while we can
    try:
        for k in keys:
            d = d[k]
    # If at any step a key is missing, return default
    except KeyError:
        return default
    # If at any step the value is not a dict...
    except TypeError:
        # ... if it's a None, return default. Assume it would be a dict.
        if d is None:
            return default
        # ... if it's something else, raise
        else:
            raise
    # If the value was found, return it
    else:
        return d
