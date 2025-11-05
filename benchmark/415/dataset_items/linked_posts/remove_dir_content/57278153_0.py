import os
files = os.listdir(yourFilePath)
for f in files:
    os.remove(yourFilePath + f)
