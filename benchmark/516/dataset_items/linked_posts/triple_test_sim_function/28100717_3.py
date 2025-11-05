mkdtemp(suffix='', prefix='tmp', dir=None)
    User-callable function to create and return a unique temporary
    directory.  The return value is the pathname of the directory.

    The directory is readable, writable, and searchable only by the
    creating user.

    Caller is responsible for deleting the directory when done with it.
