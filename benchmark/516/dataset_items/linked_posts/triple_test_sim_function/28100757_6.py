import os
import errno
if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
with open(filepath, 'w') as my_file:
    do_stuff(my_file)
