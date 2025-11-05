import glob
import os

def check_for_files(filepath):
    for filepath_object in glob.glob(filepath):
        if os.path.isfile(filepath_object):
            return True

    return False
