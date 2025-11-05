excludes= ['a\*\b', 'c\d\e']
for root, directories, files in os.walk('Start_Folder'):
    if not any(fnmatch.fnmatch(nf_root, pattern) for pattern in excludes):
        for root, directories, files in os.walk(nf_root):
            ....
            do the process
            ....
