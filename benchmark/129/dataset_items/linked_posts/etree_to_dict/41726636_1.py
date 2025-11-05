from lxml import etree
tree = etree.parse('file.xml')
root = tree.getroot()
datadict = []
for item in root:
    d = {}
    for elem in item:
        d[elem.tag]=elem.text
    datadict.append(d)
