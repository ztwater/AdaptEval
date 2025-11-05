def update(dictionary: dict[str, any], key: str, value: any, nested_dict_name: str = None) -> dict[str, any]:
    if not nested_dict_name:  # if current (outermost) dict should be updated
        if key in dictionary.keys():  # check if key exists in current dict
            dictionary[key] = value
            return dictionary
    else:  # if nested dict should be updated
        if nested_dict_name in dictionary.keys():  # check if dict is in next layer
            if isinstance(dictionary[nested_dict_name], dict):
                if key in dictionary[nested_dict_name].keys():  # check if key exists in current dict
                    dictionary[nested_dict_name][key] = value
                    return dictionary
            if isinstance(dictionary[nested_dict_name], list):
                list_index = random.choice(range(len(dictionary[nested_dict_name])))  # pick a random dict from the list

                if key in dictionary[nested_dict_name][list_index].keys():  # check if key exists in current dict
                    dictionary[nested_dict_name][list_index][key] = value
                    return dictionary

    dic_aux = []

    # this would only run IF the above if-statement was not able to identity and update a dict
    for val_aux in dictionary.values():
        if isinstance(val_aux, dict):
            dic_aux.append(val_aux)

    # call the update function again for recursion
    for i in dic_aux:
        return update(dictionary=i, key=key, value=value, nested_dict_name=nested_dict_name)
