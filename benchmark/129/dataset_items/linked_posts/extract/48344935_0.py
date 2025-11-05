from xml.parsers import expat
oldcreate = expat.ParserCreate
expat.ParserCreate = lambda encoding, sep: oldcreate(encoding, None)
