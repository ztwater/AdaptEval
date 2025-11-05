import re
badchars= re.compile(r'[^A-Za-z0-9_. ]+|^\.|\.$|^ | $|^$')
badnames= re.compile(r'(aux|com[1-9]|con|lpt[1-9]|prn)(\.|$)')

def makeName(s):
    name= badchars.sub('_', s)
    if badnames.match(name):
        name= '_'+name
    return name
