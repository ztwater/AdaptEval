>>> import re
>>> target = (
... r"this should pass v" + "\n"
... r"this is a test iii" + "\n"
... )
>>>
>>> re.findall( r"(?m)\s(i{1,3}v*|v)$", target )
['v', 'iii']
