import os
[os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser("~/files")) for f in fn]
