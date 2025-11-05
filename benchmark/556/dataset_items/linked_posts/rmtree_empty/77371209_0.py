def remove_empty_dirs(root_path):
    deleted_dirs = set()
    for current_dir, subdirs, files in os.walk(root_path, topdown=False):
        still_has_subdirs = set(subdirs).intersection(deleted_dirs) != set(subdirs)

        if not files and not still_has_subdirs:
            os.rmdir(current_dir)
            deleted_dirs.add(current_dir)

    return deleted_dirs
