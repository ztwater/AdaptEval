import xml.etree.ElementTree as ET
with DisableXmlNamespaces():
     tree = ET.parse("test.xml")
