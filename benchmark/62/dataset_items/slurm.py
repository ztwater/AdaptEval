import fnmatch
import os


def include_patterns(*patterns):
    """Factory function that can be used with copytree() ignore parameter.

    Arguments define a sequence of glob-style patterns
    that are used to specify what files to NOT ignore.
    Creates and returns a function that determines this for each directory
    in the file hierarchy rooted at the source directory when used with
    shutil.copytree().
    from: https://stackoverflow.com/questions/52071642/python-copying-the-files-with-include-pattern
    """

    def _ignore_patterns(path, names):
        keep = set(
            name for pattern in patterns for name in fnmatch.filter(names, pattern)
        )
        ignore = set(
            name
            for name in names
            if name not in keep and not os.path.isdir(os.path.join(path, name))
        )
        return ignore

    return _ignore_patterns

