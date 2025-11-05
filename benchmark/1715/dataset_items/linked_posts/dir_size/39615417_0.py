>>> import os
>>> from humanize import naturalsize
>>> from glob2 import iglob
>>> naturalsize(sum(os.path.getsize(x) for x in iglob('/var/**'))))
'546.2 MB'
