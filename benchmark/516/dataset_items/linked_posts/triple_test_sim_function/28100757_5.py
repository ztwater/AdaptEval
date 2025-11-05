import os
if not os.path.exists(directory):
    os.makedirs(directory)
with open(filepath, 'w') as my_file:
    do_stuff(my_file)
