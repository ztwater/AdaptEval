import os

directory = r'path-to-directory'

for entry in os.scandir(directory):
    if os.path.isdir(entry.path) and not os.listdir(entry.path) :
        os.rmdir(entry.path)
