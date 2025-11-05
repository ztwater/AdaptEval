import os
folder = 'C:/Dropbox'
file_count = sum(len(files) for _, _, files in os.walk(folder))
print(file_count)
