from lxml import etree

source = "input.xml"

with open(source, 'rb') as source:
    parser = etree.XMLParser(encoding = "iso-8859-1")
    root = etree.parse(source, parser)
      
string = etree.tostring(root, xml_declaration = True, encoding="UTF-8", pretty_print=True).decode('utf8').encode('iso-8859-1')

with open('output.xml', 'wb') as target:
    target.write(string)
