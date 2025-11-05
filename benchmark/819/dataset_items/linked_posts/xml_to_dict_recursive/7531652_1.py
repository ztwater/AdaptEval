>>> from xmlloader import *
>>> example = file('example.xml', 'r')   # A document containing XML
>>> xl = StreamXMLLoader(example, 0)     # 0 = all defaults on operation
>>> result = xl.expect XML()
>>> print result
{'top': {'a': '1', 'c': 'three', 'b': '2.2'}}
