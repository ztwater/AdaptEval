import os
import errno

try:
    os.makedirs(<path>)
except OSError as e:
    if errno.EEXIST != e.errno:
        raise
