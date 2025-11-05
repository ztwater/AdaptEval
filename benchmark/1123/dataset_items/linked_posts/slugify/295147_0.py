import re

str = "File!name?.txt"
f = open(os.path.join("/tmp", re.sub('[^-a-zA-Z0-9_.() ]+', '', str))
