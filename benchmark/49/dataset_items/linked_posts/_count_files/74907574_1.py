import os
file_count = sum(len([f for f in files if f.endswith('.svg')]) for _, _, files in os.walk(folder))
print(file_count)
