import os
import string
drive = string.ascii_uppercase
valid_drives = []
for each_drive in drive:
    if os.path.exist(each_drive+":\\"):
       print(each_drive)
       valid_drives.append(each_drive+":\\")
print(valid_drives)
