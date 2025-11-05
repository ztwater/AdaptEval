xmlns = '{http://foo.namespaceinfo.com}'

def etree_to_dict(t):
    if xmlns in t.tag:
        t.tag = t.tag.lstrip(xmlns)
    if d = {t.tag : map(etree_to_dict, t.iterchildren())}
    d.update(('@' + k, v) for k, v in t.attrib.iteritems())
    d['text'] = t.text
    return d
