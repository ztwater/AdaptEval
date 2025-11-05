import os
import shutil

with os.scandir(target_dir) as entries:
    for entry in entries:
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry.path)
        else:
            os.remove(entry.path)
