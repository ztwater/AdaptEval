from lxml import etree
e = etree.XML(xml)
xmltodict.parse(etree.tostring(e))
