from lxml import objectify as xml_objectify


def xml_to_dict(xml_str):
    """ Convert xml to dict, using lxml v3.4.2 xml processing library """
    def xml_to_dict_recursion(xml_object):
        dict_object = xml_object.__dict__
        if not dict_object:
            return xml_object
        for key, value in dict_object.items():
            dict_object[key] = xml_to_dict_recursion(value)
        return dict_object
    return xml_to_dict_recursion(xml_objectify.fromstring(xml_str))

xml_string = """<?xml version="1.0" encoding="UTF-8"?><Response><NewOrderResp>
<IndustryType>Test</IndustryType><SomeData><SomeNestedData1>1234</SomeNestedData1>
<SomeNestedData2>3455</SomeNestedData2></SomeData></NewOrderResp></Response>"""

print xml_to_dict(xml_string)
