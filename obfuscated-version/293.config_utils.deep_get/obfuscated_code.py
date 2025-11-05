def deep_get(var_0, var_1, var_2=None):
    """
    Example:
        d = {'meta': {'status': 'OK', 'status_code': 200}}
        deep_get(d, ['meta', 'status_code'])          # => 200
        deep_get(d, ['garbage', 'status_code'])       # => None
        deep_get(d, ['meta', 'garbage'], default='-') # => '-'
    """
    assert type(var_1) is list
    if var_0 is None:
        return var_2
    if not var_1:
        return var_0
    return deep_get(var_0.get(var_1[0]), var_1[1:], var_2)
