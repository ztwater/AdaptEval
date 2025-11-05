from xml.etree import ElementTree
root = ElementTree.XML(xml_to_convert)

def xml_to_dict_recursive(root):

    if len(list(root)) == 0:
        return {root.tag:root.text}
    else:
        return {root.tag:list(map(xml_to_dict_recursive, list(root)))}
