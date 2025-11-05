import sys

# cs = case sensitive
# ys = whatever you want to be "yes" - string or tuple of strings

#  prompt('promptString') == 1:               # only y
#  prompt('promptString',cs = 0) == 1:        # y or Y
#  prompt('promptString','Yes') == 1:         # only Yes
#  prompt('promptString',('y','yes')) == 1:   # only y or yes
#  prompt('promptString',('Y','Yes')) == 1:   # only Y or Yes
#  prompt('promptString',('y','yes'),0) == 1: # Yes, YES, yes, y, Y etc.

def prompt(ps,ys='y',cs=1):
    sys.stdout.write(ps)
    ii = raw_input()
    if cs == 0:
        ii = ii.lower()
    if type(ys) == tuple:
        for accept in ys:
            if cs == 0:
                accept = accept.lower()
            if ii == accept:
                return True
    else:
        if ii == ys:
            return True
    return False
