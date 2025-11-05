import os
mypath = "my_folder" #Enter your path here
for root, dirs, files in os.walk(mypath, topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))

    # Add this block to remove folders
    for dir in dirs:
        os.rmdir(os.path.join(root, dir))

# Add this line to remove the root folder at the end
os.rmdir(mypath)
