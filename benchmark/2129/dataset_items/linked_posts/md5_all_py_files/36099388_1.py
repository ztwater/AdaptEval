import glob
import hashlib
file = glob.glob("/root/PycharmProjects/untitled1/*.exe")

for f in file:
    with open(f, 'rb') as getmd5:
        data = getmd5.read()
        gethash = hashlib.md5(data).hexdigest()
        print("f: " + gethash)
