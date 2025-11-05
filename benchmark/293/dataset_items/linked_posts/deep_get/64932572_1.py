def get_keys(_dict: dict, prefix: list):
    prefix += list(_dict.keys())
    return prefix


def _loop_elements(elems:list, prefix=None, limit=None):
    prefix = prefix or []
    limit = limit or 9
    try:
        if len(elems) != 0 and isinstance(elems, list):
            for _ in elems:
                if isinstance(_, dict):
                    get_keys(_, prefix)
                    for item in _.values():
                        _loop_elements(item, prefix, limit)
        return prefix[:limit]
    except TypeError:
        return


>>>goo = _loop_elements(foo,limit=9)
>>>goo
['feature_name', 'scenarios', 'scenario_name', 'scenario_status', 'scenario_tags', 'steps', 'duration', 'name', 'status']
