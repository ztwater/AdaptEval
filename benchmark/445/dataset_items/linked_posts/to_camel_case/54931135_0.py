import re

f = open("in.txt", "r")
words = f.read()

def to_camel_case3(s):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s)

f = open("out.txt", "w")
f.write(to_camel_case3(words))
