try:
    os.makedirs("path/to/directory")
except FileExistsError:
    # directory already exists
    pass
