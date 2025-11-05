def deep_get(_dict, keys, default=None):
    def _reducer(d, key):
        if isinstance(d, dict):
            return d.get(key, default)
        if isinstance(d, list):
            return d[key] if len(d) > 0 else default
        return default
    return reduce(_reducer, keys, _dict)
