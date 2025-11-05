sum([sum(map(lambda fname: os.path.getsize(os.path.join(directory, fname)), files)) for directory, folders, files in os.walk(path)])
