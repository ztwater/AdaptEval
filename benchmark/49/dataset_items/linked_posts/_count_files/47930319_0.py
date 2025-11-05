import os

file_count = sum(len(files) for _, _, files in os.walk(r'C:\Dropbox'))
print(file_count)
