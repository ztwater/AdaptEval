ns= {'xml_test':'http://www.test.com'}
tree = ET.parse(r"test.xml")
el1 = tree.findall("xml_test:DEAL_LEVEL/xml_test:PAID_OFF",ns)
