import os

def listFiles(self, dir_name):
    names = []
    for root, directory, files in os.walk(dir_name):
        if root == dir_name:
            for name in files:
                names.append(name)
    return names
