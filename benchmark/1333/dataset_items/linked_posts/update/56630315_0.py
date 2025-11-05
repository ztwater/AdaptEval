def update_values_dict(original_dict, future_dict, old_value, new_value):
    # Recursively updates values of a nested dict by performing recursive calls

    if isinstance(original_dict, Dict):
        # It's a dict
        tmp_dict = {}
        for key, value in original_dict.items():
            tmp_dict[key] = update_values_dict(value, future_dict, old_value, new_value)
        return tmp_dict
    elif isinstance(original_dict, List):
        # It's a List
        tmp_list = []
        for i in original_dict:
            tmp_list.append(update_values_dict(i, future_dict, old_value, new_value))
        return tmp_list
    else:
        # It's not a dict, maybe a int, a string, etc.
        return original_dict if original_dict != old_value else new_value
