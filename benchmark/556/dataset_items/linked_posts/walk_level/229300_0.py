def _dir_list(self, dir_name, whitelist):
    outputList = []
    for root, dirs, files in os.walk(dir_name):
        dirs[:] = [d for d in dirs if is_good(d)]
        for f in files:
            do_stuff()
