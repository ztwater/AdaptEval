import glob
import hashlib

filenames = glob.glob("/root/PycharmProjects/untitled1/*.exe")

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        print(filename, hashlib.md5(data).hexdigest())
