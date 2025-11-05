import os

from typing import MutableSet

def rmtree_empty(root: str) -> MutableSet[str]:
    """
    Delete empty directories in tree.
    Returns set of deleted directories.
    """
    # Source: https://stackoverflow.com/a/65624165
    # Need to cache deleted directories, because os.walk only evaluates child folders once when calling
    # and then goes through cached folder list.
    deleted = set()

    for current_dir, subdirs, files in os.walk(root, topdown=False):
        # has any files?
        if any(files):
            continue

        # has not deleted subdir?
        if any(os.path.join(current_dir, subdir)
               not in deleted for subdir in subdirs):
            continue

        os.rmdir(current_dir)
        deleted.add(current_dir)

    return deleted

