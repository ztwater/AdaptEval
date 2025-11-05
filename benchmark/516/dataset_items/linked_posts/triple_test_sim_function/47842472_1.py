# ----------------------------------------------------------------------------
# [1] https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist

import pathlib

""" Notes:
        1.  Include a trailing slash at the end of the directory path
            ("Method 1," below).
        2.  If a subdirectory in your intended path matches an existing file
            with same name, you will get the following error:
            "NotADirectoryError: [Errno 20] Not a directory:" ...
"""
# Uncomment and try each of these "out_dir" paths, singly:

# ----------------------------------------------------------------------------
# METHOD 1:
# Re-running does not overwrite existing directories and files; no errors.

# out_dir = 'output/corpus3'                ## no error but no dir created (missing tailing /)
# out_dir = 'output/corpus3/'               ## works
# out_dir = 'output/corpus3/doc1'           ## no error but no dir created (missing tailing /)
# out_dir = 'output/corpus3/doc1/'          ## works
# out_dir = 'output/corpus3/doc1/doc.txt'   ## no error but no file created (os.makedirs creates dir, not files!  ;-)
# out_dir = 'output/corpus2/tfidf/'         ## fails with "Errno 20" (existing file named "corpus2")
# out_dir = 'output/corpus3/tfidf/'         ## works
# out_dir = 'output/corpus3/a/b/c/d/'       ## works

# [2] https://docs.python.org/3/library/os.html#os.makedirs

# Uncomment these to run "Method 1":

#directory = os.path.dirname(out_dir)
#os.makedirs(directory, mode=0o777, exist_ok=True)

# ----------------------------------------------------------------------------
# METHOD 2:
# Re-running does not overwrite existing directories and files; no errors.

# out_dir = 'output/corpus3'                ## works
# out_dir = 'output/corpus3/'               ## works
# out_dir = 'output/corpus3/doc1'           ## works
# out_dir = 'output/corpus3/doc1/'          ## works
# out_dir = 'output/corpus3/doc1/doc.txt'   ## no error but creates a .../doc.txt./ dir
# out_dir = 'output/corpus2/tfidf/'         ## fails with "Errno 20" (existing file named "corpus2")
# out_dir = 'output/corpus3/tfidf/'         ## works
# out_dir = 'output/corpus3/a/b/c/d/'       ## works

# Uncomment these to run "Method 2":

#import os, errno
#try:
#       os.makedirs(out_dir)
#except OSError as e:
#       if e.errno != errno.EEXIST:
#               raise
# ----------------------------------------------------------------------------
