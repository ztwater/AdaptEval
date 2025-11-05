import os
try:
    os.makedirs('./path/to/somewhere')
except OSError:
    pass
