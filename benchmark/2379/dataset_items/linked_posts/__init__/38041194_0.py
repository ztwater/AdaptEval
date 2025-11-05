from xml.dom import minidom

SNOWMAN = '&#x2603;&#xfe0e;'

imp = minidom.getDOMImplementation()
dom = imp.createDocument(None, 'root', None)
