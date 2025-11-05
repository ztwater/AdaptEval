# python 2
def gen_dict_extract(key, var):
    if hasattr(var,'iteritems'): # hasattr(var,'items') for python 3
        for k, v in var.iteritems(): # var.items() for python 3
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result
