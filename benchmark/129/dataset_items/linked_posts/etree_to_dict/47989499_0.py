import xmltodict

xml = '''
<root>
  <e />
  <e>text</e>
  <e name="value" />
  <e name="value">text</e>
  <e> <a>text</a> <b>text</b> </e>
  <e> <a>text</a> <a>text</a> </e>
  <e> text <a>text</a> </e>
</root>
'''

xdict = xmltodict.parse(xml)
