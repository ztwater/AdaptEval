from xml.etree import ElementTree as ET
tree = ET.parse("test.xml")
el1 = tree.findall("person/firstname")
print(el1[0].text)
el2 = tree.find("person/lastname")
print(el2.text)
