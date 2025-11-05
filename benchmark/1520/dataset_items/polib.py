# -* coding: utf-8 -*-
#
# License: MIT (see LICENSE file provided)
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
**polib** allows you to manipulate, create, modify gettext files (pot, po and
mo files).  You can load existing files, iterate through it's entries, add,
modify entries, comments or metadata, etc. or create new po files from scratch.

**polib** provides a simple and pythonic API via the :func:`~polib.pofile` and
:func:`~polib.mofile` convenience functions.
"""
 
import re 

 
def natural_sort(lst):
    """
    Sort naturally the given list.
    Credits: http://stackoverflow.com/a/4836734
    """
    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split('([0-9]+)', key)]

    return sorted(lst, key=alphanum_key)

# }}}
# class _BaseFile {{{

 