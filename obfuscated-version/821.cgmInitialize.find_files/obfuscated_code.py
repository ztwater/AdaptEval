import fnmatch
import os

def find_files(var_0, var_1):
    '''Return list of files matching pattern in base folder.'''
    return [n for n in fnmatch.filter(os.listdir(var_0), var_1) if
        os.path.isfile(os.path.join(var_0, n))]

