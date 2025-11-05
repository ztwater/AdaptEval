>>> test = '/* spam * spam */ eggs'
>>> import pyparsing
>>> comment = pyparsing.nestedExpr("/*", "*/").suppress()
>>> print comment.transformString(test)         
' eggs'
