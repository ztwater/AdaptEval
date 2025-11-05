def find_files(base, pattern):
    import fnmatch
    import os

    '''Return list of files matching pattern in base folder.'''
    """ http://stackoverflow.com/questions/4296138/use-wildcard-with-os-path-isfile"""
    return [n for n in fnmatch.filter(os.listdir(base), pattern) if
            os.path.isfile(os.path.join(base, n))]
