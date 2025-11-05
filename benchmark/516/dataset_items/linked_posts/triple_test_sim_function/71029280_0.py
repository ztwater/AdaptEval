import os
directory = "./out_dir/subdir1/subdir2"
if not os.path.exists(directory):
    os.makedirs(directory)
