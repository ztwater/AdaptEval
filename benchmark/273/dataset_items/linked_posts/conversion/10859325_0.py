# -*- coding: latin-1 -*-
import re
s = """0°25'30"S, 91°7'W"""

def compLat_Long(degs, mins, secs, comp_dir):
    return (degs + (mins / 60) + (secs / 3600)) * comp_dir

def extract_DegMinSec(data):   
    m = re.search(r'(\d+°)*(\d+\')*(\d+")*', data.strip())
    deg, mins, secs = [0.0 if m.group(i) is None else float(m.group(i)[:-1]) for i in range(1, 4)]
    comp_dir = 1 if data[-1] in ('W', 'S') else -1
    return deg, mins, secs, comp_dir 

s1, s2 = s.split(',')
dms1 = extract_DegMinSec(s1)
dms2 = extract_DegMinSec(s2)
print('{:7.4f}  {:7.4f}'.format(compLat_Long(*dms1), compLat_Long(*dms2)))
