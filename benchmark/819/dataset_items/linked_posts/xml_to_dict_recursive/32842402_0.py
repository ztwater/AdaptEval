def etree_to_ordereddict(t):
d = OrderedDict()
d[t.tag] = OrderedDict() if t.attrib else None
children = list(t)
if children:
    dd = OrderedDict()
    for dc in map(etree_to_ordereddict, children):
        for k, v in dc.iteritems():
            if k not in dd:
                dd[k] = list()
            dd[k].append(v)
    d = OrderedDict()
    d[t.tag] = OrderedDict()
    for k, v in dd.iteritems():
        if len(v) == 1:
            d[t.tag][k] = v[0]
        else:
            d[t.tag][k] = v
if t.attrib:
    d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
if t.text:
    text = t.text.strip()
    if children or t.attrib:
        if text:
            d[t.tag]['#text'] = text
    else:
        d[t.tag] = text
return d
