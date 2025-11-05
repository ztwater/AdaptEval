from scandir import scandir
def getTotFldrSize(path):
    return sum([s.stat(follow_symlinks=False).st_size for s in scandir(path) if s.is_file(follow_symlinks=False)]) + \
    + sum([getTotFldrSize(s.path) for s in scandir(path) if s.is_dir(follow_symlinks=False)])

>>> print getTotFldrSize('.')
1203245680
