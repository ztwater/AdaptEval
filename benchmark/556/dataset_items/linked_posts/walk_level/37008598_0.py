for path, dirs, files in os.walk('.'):
    print path, dirs, files
    del dirs[:] # go only one level deep
