from xml.etree import cElementTree as ElementTree

def xml_to_dict(xml, result):
    for child in xml:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(xml_to_dict(child, {}))
            else:
                result[child.tag] = xml_to_dict(child, {})
    return result

xmlTree = ElementTree.parse('my_file.xml')
xmlRoot = xmlTree.getroot()
dictRoot = xml_to_dict(xmlRoot, {})
result = {xmlRoot.tag: dictRoot}

