import io
import xml.etree.ElementTree as ET

# instead of ET.fromstring(xml)
it = ET.iterparse(io.StringIO(xml))
for _, el in it:
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    for at in list(el.attrib.keys()): # strip namespaces of attributes too
        if '}' in at:
            newat = at.split('}', 1)[1]
            el.attrib[newat] = el.attrib[at]
            del el.attrib[at]
root = it.root
