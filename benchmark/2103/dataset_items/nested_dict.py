from typing import Dict

def append_nested_dict(dict1: Dict, dict2: Dict) -> None:
    """
    Recursively walk through two dicts to append dict2 to dict1.

    Mutates dict1

    Modified from:
    https://stackoverflow.com/a/58742155

    Parameters
    ----------
    dict1 : nested dict
        Nested dict to be appended to
    dict2 : nested dict
        Nested dict to append

    """
    for key, val in dict1.items():
        if isinstance(val, dict):
            if key in dict2 and isinstance(dict2[key], dict):
                append_nested_dict(dict1[key], dict2[key])
        else:
            if key in dict2:
                dict1[key] = dict2[key]

    for key, val in dict2.items():
        if key not in dict1:
            dict1[key] = val
