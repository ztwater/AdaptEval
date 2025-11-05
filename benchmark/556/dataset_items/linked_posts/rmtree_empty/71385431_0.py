import os
import shutil

def purge_dir(dir, in_place=False):

    deleted = []
    dir_tree = list(os.walk(dir, topdown=False))

    for tree_element in dir_tree:
        sub_dir = tree_element[0]
        is_empty = not len(os.listdir(sub_dir))
        if is_empty:
            deleted.append(sub_dir)

    if in_place:
        list(map(os.rmdir, deleted))

    return deleted
