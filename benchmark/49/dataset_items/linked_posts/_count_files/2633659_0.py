import os

def count_files(in_directory):
    joiner= (in_directory + os.path.sep).__add__
    return sum(
        os.path.isfile(filename)
        for filename
        in map(joiner, os.listdir(in_directory))
    )

>>> count_files("/usr/lib")
1797
>>> len(os.listdir("/usr/lib"))
2049
