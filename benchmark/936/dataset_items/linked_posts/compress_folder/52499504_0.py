import os
import zipfile

def zipall(ob, path, rel=""):
    basename = os.path.basename(path)
    if os.path.isdir(path):
        if rel == "":
            rel = basename
        ob.write(path, os.path.join(rel))
        for root, dirs, files in os.walk(path):
            for d in dirs:
                zipall(ob, os.path.join(root, d), os.path.join(rel, d))
            for f in files:
                ob.write(os.path.join(root, f), os.path.join(rel, f))
            break
    elif os.path.isfile(path):
        ob.write(path, os.path.join(rel, basename))
    else:
        pass
