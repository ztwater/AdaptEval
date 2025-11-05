import os

def folder_size(path):
    parent = {}  # path to parent path mapper
    folder_size = {}  # storing the size of directories
    folder = os.path.realpath(path)

    for root, _, filenames in os.walk(folder):
        if root == folder:
            parent[root] = -1  # the root folder will not have any parent
            folder_size[root] = 0.0  # intializing the size to 0

        elif root not in parent:
            immediate_parent_path = os.path.dirname(root)  # extract the immediate parent of the subdirectory
            parent[root] = immediate_parent_path  # store the parent of the subdirectory
            folder_size[root] = 0.0  # initialize the size to 0

        total_size = 0
        for filename in filenames:
            filepath = os.path.join(root, filename)
            total_size += os.stat(filepath).st_size  # computing the size of the files under the directory
        folder_size[root] = total_size  # store the updated size

        temp_path = root  # for subdirectories, we need to update the size of the parent till the root parent
        while parent[temp_path] != -1:
            folder_size[parent[temp_path]] += total_size
            temp_path = parent[temp_path]

    return folder_size[folder]/1000000.0
