import os

def remove_empty_directories(root):
    for dirpath, dirnames, filenames in os.walk(root):
        if not filenames and not dirnames:
            os.rmdir(dirpath)
