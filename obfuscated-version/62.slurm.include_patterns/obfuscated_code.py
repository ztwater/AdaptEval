def include_patterns(*var_0):
    """Factory function that can be used with copytree() ignore parameter.

    Arguments define a sequence of glob-style patterns
    that are used to specify what files to NOT ignore.
    Creates and returns a function that determines this for each directory
    in the file hierarchy rooted at the source directory when used with
    shutil.copytree().
    """
    def _ignore_patterns(var_1, var_2):
        var_3 = set(name for pattern in var_0
                            for name in filter(var_2, pattern))
        var_4 = set(name for name in var_2
                        if name not in var_3 and not isdir(join(var_1, name)))
        return var_4
    return _ignore_patterns

