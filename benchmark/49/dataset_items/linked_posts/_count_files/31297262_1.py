import os

onlyfiles = next(os.walk(directory))[2] #directory is your directory path as string
print len(onlyfiles)
