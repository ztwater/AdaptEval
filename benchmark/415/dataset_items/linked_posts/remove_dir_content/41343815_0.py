import os

def recursively_remove_files(f):
    if os.path.isfile(f):
        os.unlink(f)
    elif os.path.isdir(f):
        for fi in os.listdir(f):
            recursively_remove_files(os.path.join(f, fi))

recursively_remove_files(my_directory)
