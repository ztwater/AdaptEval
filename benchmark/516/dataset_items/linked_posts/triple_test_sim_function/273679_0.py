import os

dirname = 'create/me'

try:
    os.makedirs(dirname)
except OSError:
    if os.path.exists(dirname):
        # We are nearly safe
        pass
    else:
        # There was an error on creation, so make sure we know about it
        raise
