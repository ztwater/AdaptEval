import xml.etree.ElementTree as ET
root = ET.parse(xml_filepath).getroot()

def parse_xml(node):
    ans = {}
    for child in node:
        if len(child) == 0:
            ans[child.tag] = child.text
        elif child.tag not in ans:
            ans[child.tag] = parse_xml(child)
        elif not isinstance(ans[child.tag], list):
            ans[child.tag] = [ans[child.tag]]
            ans[child.tag].append(parse_xml(child))
        else:
            ans[child.tag].append(parse_xml(child))
    return ans
