for path, subdirs, files in os.walk(dir_name):
    for name in files:
        if path == ".": #this will filter the files in the current directory
             #code here
