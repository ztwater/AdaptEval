from collections.abc import Mapping
from typing import Dict

def update_dict(d: Dict, u: Mapping) -> Dict:
    """
    Update a dictionary with another dictionary.
    Source: https://stackoverflow.com/a/3233356/8702341
    """
    for k, v in u.items():
        if isinstance(v, Mapping):
            d[k] = update_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d

