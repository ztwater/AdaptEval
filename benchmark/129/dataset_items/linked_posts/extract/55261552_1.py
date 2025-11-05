import _elementtree
try:
    del _elementtree.XMLParser
except AttributeError:
    # in case deleted twice
    pass
else:
    from xml.parsers import expat  # NOQA: F811
    oldcreate = expat.ParserCreate
    expat.ParserCreate = lambda encoding, sep: oldcreate(encoding, None)
