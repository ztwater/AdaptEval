from collections import defaultdict
def xml2dict(node):
    d, count = defaultdict(list), 1
    for i in node:
        d[i.tag + "_" + str(count)]['text'] = i.findtext('.')[0]
        d[i.tag + "_" + str(count)]['attrib'] = i.attrib # attrib gives the list
        d[i.tag + "_" + str(count)]['children'] = xml2dict(i) # it gives dict
     return d
