def get(obj, key: str | int, default=None):
    """
    Try to get index, key or a property
    for a given list, dict or object,
    returns default on error
    
    Args:
        - obj (mixed): dict, list, object
        - key (str):  either any key or dot accessor like: foo.bar.0
    Returns:
        - mixed | None
    """

    key = str(key)
    keys = [key]
    if '.' in key:
        keys = key.split('.')

    val = obj
    for k in keys:
        if not k:
            continue

        try:
            if isinstance(val, list):
                val = val[k]
            elif isinstance(val, dict):
                val = val.get(k, default)
            else:
                val = getattr(val, k, default)
        except (IndexError, KeyError, AttributeError, TypeError, ValueError) as e:
            if 'list indices must be integers or slices, not str' in str(e):
                try:
                    k = int(k)
                    val = val[k]
                except (ValueError, KeyError, IndexError):
                    val = default
            else:
                return default

    return val
