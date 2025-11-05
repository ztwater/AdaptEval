from collections import OrderedDict
from typing import Union
from xml.etree.ElementTree import ElementTree, Element

def etree_to_dict(root: Union[ElementTree, Element], include_root_tag=False):
    root = root.getroot() if isinstance(root, ElementTree) else root
    result = OrderedDict()
    if len(root) > 1 and len({child.tag for child in root}) == 1:
        result[next(iter(root)).tag] = [etree_to_dict(child) for child in root]
    else:
        for child in root:
            result[child.tag] = etree_to_dict(child) if len(list(child)) > 0 else (child.text or "")
    result.update(('@' + k, v) for k, v in root.attrib.items())
    return {root.tag: result} if include_root_tag else result

d = etree_to_dict(etree.ElementTree.parse('data.xml'), True)
