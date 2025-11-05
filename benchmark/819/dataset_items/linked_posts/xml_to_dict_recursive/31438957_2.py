def xml_to_dict(xml_str):
    """ Convert xml to dict, using lxml v3.4.2 xml processing library, see http://lxml.de/ """
    def xml_to_dict_recursion(xml_object):
        dict_object = xml_object.__dict__
        if not dict_object:  # if empty dict returned
            return xml_object
        for key, value in dict_object.items():
            dict_object[key] = xml_to_dict_recursion(value)
        return dict_object
    xml_obj = objectify.fromstring(xml_str)
    return {xml_obj.tag: xml_to_dict_recursion(xml_obj)}
