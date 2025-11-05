from io import StringIO  # for Python 2 import from StringIO instead
import xml.etree.ElementTree as ET

# instead of ET.fromstring(xml)
it = ET.iterparse(StringIO(xml))
for _, el in it:
    _, _, el.tag = el.tag.rpartition('}') # strip ns
root = it.root
