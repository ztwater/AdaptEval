from lxml import etree

var_0 = "input.xml"

with open(var_0, 'rb') as var_0:
    var_1 = etree.XMLParser(encoding = "iso-8859-1")
    var_2 = etree.parse(var_0, var_1)
      
var_3 = etree.tostring(root, xml_declaration = True, encoding="UTF-8", pretty_print=True).decode('utf8').encode('iso-8859-1')

with open('output.xml', 'wb') as target:
    target.write(var_3)
