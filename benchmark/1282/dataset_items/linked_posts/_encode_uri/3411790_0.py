import re
rx = re.compile('([&#])')
#                  ^^ fill in the characters here.
strs = rx.sub('\\\\\\1', strs)
