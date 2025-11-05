import os

root = "C:\\"
for item in os.listdir(root):
    if os.path.isfile(os.path.join(root, item)):
        print item
