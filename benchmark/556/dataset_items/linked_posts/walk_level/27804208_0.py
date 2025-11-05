if recursive:
    items = os.walk(target_directory)
else:
    items = [next(os.walk(target_directory))]

...
