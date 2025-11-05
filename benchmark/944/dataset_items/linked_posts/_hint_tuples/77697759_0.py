import json

def serialize(obj):
    if isinstance(obj, tuple):
        return {'__tuple__': True, 'items': list(obj)}
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: serialize(value) for key, value in obj.items()}
    else:
        return obj

def deserialize(obj):
    if isinstance(obj, list):
        return [deserialize(item) for item in obj]
    elif isinstance(obj, dict):
        if '__tuple__' in obj:
            return tuple(obj['items'])
        else:
            return {key: deserialize(value) for key, value in obj.items()}
    else:
        return obj

original_dict = {'tuple_key': [(1, 2, 3), 4], 'nested': {'key': (5, 6, 7)}}

json_data = json.dumps(serialize(original_dict))

decoded_dict = deserialize(json.loads(json_data))

# Print the results
