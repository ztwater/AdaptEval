import os

def mkdir_recursive(path):
    #https://stackoverflow.com/questions/6004073/how-can-i-create-directories-recursively
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path):
        mkdir_recursive(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)
        