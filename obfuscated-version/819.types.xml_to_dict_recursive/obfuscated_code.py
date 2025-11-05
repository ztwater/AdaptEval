def xml_to_dict_recursive(var_0):

    if len(list(var_0)) == 0:
        return {var_0.tag:var_0.text}
    else:
        return {var_0.tag:list(map(xml_to_dict_recursive, list(var_0)))}
