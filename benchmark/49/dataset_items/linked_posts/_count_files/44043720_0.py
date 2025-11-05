def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])
