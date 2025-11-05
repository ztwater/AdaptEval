from collections import defaultdict
from xml.etree import ElementTree


def etree_to_dict(e: ElementTree.Element) -> dict:
    """Recursively converts an ElementTree.Element into a dictionary.

    Element attributes are stored into `"@"`-prefixed attribute keys.
    Element text is stored into `"#text"` for all nodes.

    From https://stackoverflow.com/a/10076823.
    """
    d = {e.tag: {} if e.attrib else None}
    children = list(e)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {e.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if e.attrib:
        d[e.tag].update(("@" + k, v) for k, v in e.attrib.items())
    if e.text:
        text = e.text.strip()
        if children or e.attrib:
            if text:
                d[e.tag]["#text"] = text
        else:
            d[e.tag] = text
    return d

