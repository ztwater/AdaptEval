from typing import Iterator

# def gen_dict_extract(var, keys):
#     for key in keys:
#       if hasattr(var, 'items'):
#          for k, v in var.items():
#             if k == key:
#                yield v
#             if isinstance(v, dict):
#                for result in gen_dict_extract([key], v):
#                   yield result
#             elif isinstance(v, list):
#                for d in v:
#                   for result in gen_dict_extract([key], d):
#                      yield result
# def gen_dict_extract(key_, dict_):
def gen_dict_extract(key_: str, dict_: dict) -> Iterator:
    """
    Returns all values for the provided key in dict
    Source: https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists
    :param str key_:
    :param dict dict_:
    :return:
    """
    if hasattr(dict_, "items"):
        for k, v in dict_.items():
            if k == key_:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key_, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key_, d):
                        yield result

