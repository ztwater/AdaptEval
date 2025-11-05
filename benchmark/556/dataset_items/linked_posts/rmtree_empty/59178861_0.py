import os
import shutil

if len(os.listdir(folder_path)) == 0: # Check if the folder is empty
    shutil.rmtree(folder_path) # If so, delete it
