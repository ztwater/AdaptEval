from xml.etree import cElementTree as ET
e = ET.XML('''
<root>
  <e />
  <e>text</e>
  <e name="value" />
  <e name="value">text</e>
  <e> <a>text</a> <b>text</b> </e>
  <e> <a>text</a> <a>text</a> </e>
  <e> text <a>text</a> </e>
</root>
''')

from pprint import pprint
pprint(etree_to_ordereddict(e))
