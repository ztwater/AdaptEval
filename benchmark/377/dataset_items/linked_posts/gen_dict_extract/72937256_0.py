def get_ids(data: Dict, key: str) -> List:
    stack = [data]
    result = []
    while stack:
        elem = stack.pop()
        if isinstance(elem, dict):
            for k, v in elem.items():
                if k == key:
                    result.append(v)
                if isinstance(elem, (list, dict)):
                    stack.append(v)
        elif isinstance(elem, list):
            for obj in elem:
                stack.append(obj)
    return result
