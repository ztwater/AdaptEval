import os
def fcount(path):
    #Counts the number of files in a directory
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1

    return count
path = r"C:\Users\EE EKORO\Desktop\Attack_Data" #Read files in folder
print (fcount(path))
