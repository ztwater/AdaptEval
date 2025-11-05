for root, dirs, files in os.walk(directory):
    if level > 0:
        # do some stuff
    else:
        break
    level-=1
