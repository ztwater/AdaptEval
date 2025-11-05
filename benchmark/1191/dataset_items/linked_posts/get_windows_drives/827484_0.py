import os, re
re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)
