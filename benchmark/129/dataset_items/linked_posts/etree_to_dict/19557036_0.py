def etree_to_dict(t):
    return {t.tag : map(etree_to_dict, t.iterchildren()) or t.text}
