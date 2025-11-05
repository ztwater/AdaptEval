tree = ElementTree.parse('your_file.xml')
root = tree.getroot()
xmldict = XmlDictConfig(root)
