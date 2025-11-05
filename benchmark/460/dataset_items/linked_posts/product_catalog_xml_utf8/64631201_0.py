myFileIn = 'ISO_8859_1.xml'
myFileOu = 'utf_8.xml'

from xml.etree import ElementTree

#  open in binary mode ↓
with open( myFileIn, 'rb') as f:
    root = ElementTree.fromstring( f.read())

tree = ElementTree.ElementTree( root)
tree.write( myFileOu, encoding="utf-8", xml_declaration=True)
