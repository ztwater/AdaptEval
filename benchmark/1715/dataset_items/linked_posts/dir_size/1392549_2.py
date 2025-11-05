import os

nbytes = sum(d.stat().st_size for d in os.scandir('.') if d.is_file())
