from lxml import etree
from pprint import pprint

xml_f = b"""<?xml version="1.0" encoding="UTF-8"?>
            <Data>
              <Person>
                <First>John</First>
                <Last>Smith</Last>
              </Person>
              <Person>
                <First>Jane</First>
                <Last>Doe</Last>
              </Person>
            </Data>"""

elm = etree.fromstring(xml_f)
d = XmlDict.xml2dict(elm)
