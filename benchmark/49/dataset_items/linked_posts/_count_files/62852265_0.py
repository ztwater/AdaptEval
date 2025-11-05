def count_files(path):
    return sum([len(files) for _, _, files in os.walk(path)])

count_files('path/to/dir')
