from xml.etree import ElementTree

# Replace xml_to_convert below
root = ElementTree.XML(xml_to_convert)

def xml_to_dict(root):
    if len(root):
        return {root.tag:{k:v for d in map(xml_to_dict, root)
                              for k,v in d.items() }}
    else:
        return {root.tag:root.text}
