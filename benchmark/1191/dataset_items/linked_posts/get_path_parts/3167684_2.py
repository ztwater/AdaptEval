folders = []
while 1:
    path, folder = os.path.split(path)

    if folder != "":
        folders.append(folder)
    else:
        if path != "":
            folders.append(path)

        break

folders.reverse()
