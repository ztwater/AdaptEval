#LOOP THROUGH ALL SUBFOLDERS FIRST

import os
root = os.getcwd() #CHANGE THIS TO PATH IF REQUIRED
folders = sorted(list(os.walk(root))[1:],reverse=True)
for folder in folders:
    try:
        os.rmdir(folder[0])
    except OSError as error: 
        print("Directory '{}' can not be removed".format(folder[0])) 
