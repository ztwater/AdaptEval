import os
import stat

size = 0
path_ = ""
def calculate(path=os.environ["SYSTEMROOT"]):
    global size, path_
    size = 0
    path_ = path

    for x, y, z in os.walk(path):
        for i in z:
            size += os.path.getsize(x + os.sep + i)

def cevir(x):
    global path_
    print(path_, x, "Byte")
    print(path_, x/1024, "Kilobyte")
    print(path_, x/1048576, "Megabyte")
    print(path_, x/1073741824, "Gigabyte")

calculate("C:\Users\Jundullah\Desktop")
cevir(size)

Output:
C:\Users\Jundullah\Desktop 87874712211 Byte
C:\Users\Jundullah\Desktop 85815148.64355469 Kilobyte
C:\Users\Jundullah\Desktop 83803.85609722137 Megabyte
C:\Users\Jundullah\Desktop 81.83970321994275 Gigabyte
