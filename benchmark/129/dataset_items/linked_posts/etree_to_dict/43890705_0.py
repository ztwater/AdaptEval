import xml.etree.ElementTree as ET

xml = ('<xml>' +
       '<first_name>Dean Christian</first_name>' +
       '<middle_name>Christian</middle_name>' +
       '<last_name>Armada</last_name>' +
       '</xml>')
root = ET.fromstring(xml)

x = {x.tag: root.find(x.tag).text  for x in root._children}
# returns {'first_name': 'Dean Christian', 'last_name': 'Armada', 'middle_name': 'Christian'}
