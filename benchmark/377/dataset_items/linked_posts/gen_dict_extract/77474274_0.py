def extract(var, key, context_keys=(), xpath=''):
    if isinstance(var, dict):
        if key in var:
            yield {f'{xpath}.{key}': var[key]} | {f'{xpath}.{key}': value for key, value in var.items() if key in context_keys}
        for subkey, value in var.items():
            yield from extract(value, key, context_keys, f'{xpath}.{subkey}')
    elif isinstance(var, list):
        for i, elem in enumerate(var):
            yield from extract(elem, key, context_keys, f'{xpath}[{i}]')
