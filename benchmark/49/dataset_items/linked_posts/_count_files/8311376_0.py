import os

_, _, files = next(os.walk("/usr/lib"))
file_count = len(files)
