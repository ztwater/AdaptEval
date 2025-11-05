module = dict()

code = """
import json

def testhi() :
    return json.dumps({"key" : "value"}, indent = 4 )
"""

exec(code, module)
x = module['testhi']()
print(x)
