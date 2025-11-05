def etree_to_dict(t):
    if type(t) is ET.ElementTree: return etree_to_dict(t.getroot())
    return {
        **t.attrib,
        'text': t.text,
        **{e.tag: etree_to_dict(e) for e in t}
    }
