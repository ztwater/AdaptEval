import os


def drop_empty_folders(directory):
    """Verify that every empty folder removed in local storage."""

    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)
