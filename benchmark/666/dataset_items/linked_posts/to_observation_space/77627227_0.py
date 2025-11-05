def new_construct(obj: Any) -> Any:
    if obj is None:
        return None
    return [] if isinstance(obj, list) else {}
 
 
def isliteral(obj: Any):
    return isinstance(obj, (int, float, str, bool))
 
 
def object_to_dict(obj):
    result = new_construct(obj)
    queue = deque([(id(obj), obj, result)])
    processed = set()
 
    while queue:
        obj_id, obj, constructed_obj = queue.pop()
        if obj_id in processed:
            continue
        processed.add(obj_id)
 
        if hasattr(obj, "__dict__"):
            obj = vars(obj)
 
        if isinstance(obj, list):
            for val in obj:
                if isliteral(val):
                    constructed_obj.append(val)
                else:
                    new_obj = new_construct(val)
                    queue.append((id(val), val, new_obj))
                    constructed_obj.append(new_obj)
        elif isinstance(obj, dict):
            for key, val in obj.items():
                if isliteral(val):
                    constructed_obj[key] = val
                else:
                    new_obj = new_construct(val)
                    constructed_obj[key] = new_obj
                    queue.append((id(val), val, new_obj))
 
    return result
