from collections import UserDict, namedtuple
from lxml.etree import QName

class XmlDict(UserDict):
    """Custom dict to avoid preceding siblings with the same name being overwritten."""

    __ROOTELM = namedtuple('RootElm', ['tag', 'node'])

    def __setitem__(self, key, value):
        if key in self:
            if type(self.data[key]) is list:
                self.data[key].append(value)
            else:
                self.data[key] = [self.data[key], value]
        else:
            self.data[key] = value

    @staticmethod
    def xml2dict(element):
        """Converts an ElementTree Element to a dictionary."""
        elm = XmlDict.__ROOTELM(
            tag=QName(element).localname,
            node=XmlDict(map(XmlDict.xml2dict, element)) or element.text,
    )
    return elm
