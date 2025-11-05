from win32.win32api import GetLogicalDriveStrings


drives = [drive for drive in GetLogicalDriveStrings()[0]]
