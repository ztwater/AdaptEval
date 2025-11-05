import os
[x for x in os.listdir("your_directory") if len(x) >= 4 and  x[-4:] == ".rar"]
