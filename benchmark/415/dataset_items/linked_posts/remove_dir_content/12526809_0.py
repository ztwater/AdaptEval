for filename in os.listdir(dirpath):
    filepath = os.path.join(dirpath, filename)
    try:
        shutil.rmtree(filepath)
    except OSError:
        os.remove(filepath)
