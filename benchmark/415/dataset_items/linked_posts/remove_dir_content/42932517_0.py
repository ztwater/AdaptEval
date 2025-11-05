if os.path.isdir(folder_location):
    shutil.rmtree(folder_location)

time.sleep(.5)

os.makedirs(folder_location, 0o777)
