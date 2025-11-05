# Import the C accelerators
try:
    # Element is going to be shadowed by the C implementation. We need to keep
    # the Python version of it accessible for some "creative" by external code
    # (see tests)
    _Element_Py = Element

    # Element, SubElement, ParseError, TreeBuilder, XMLParser
    from _elementtree import *
except ImportError:
    pass
