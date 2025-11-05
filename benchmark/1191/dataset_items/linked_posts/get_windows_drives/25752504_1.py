def get_drive():
    highest = sorted(list(set(map(chr, range(ord('A'), ord('Z')+1))) -
                          set(win32api.GetLogicalDriveStrings().split(':\\\000')[:-1])))[-1]
