def camel_to_snake(var_0):
    var_0 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', var_0)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
