import os

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if os.path.exists(fp):
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

    return total_size   # in megabytes
