def xml_to_dict(node):
    u''' 
    @param node:lxml_node
    @return: dict 
    '''

    return {'tag': node.tag, 'text': node.text, 'attrib': node.attrib, 'children': {child.tag: xml_to_dict(child) for child in node}}
