from typing import List
import platform
import string

def get_windows_drives() -> List[str]:
    """
    Returns a list of all the drives on a Windows machine. 
    See https://stackoverflow.com/questions/827371/is-there-a-way-to-list-all-the-available-windows-drives 
    for more information.
    """
    drives = []
    # Ctypes only exports windll on windows computers. 
    # Read more here: https://docs.python.org/3/library/ctypes.html#module-ctypes
    if platform.system() == 'Windows':
        from ctypes import windll # type: ignore
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                # Add :\ to the end to complete the drive. Not having :\ on the end causes os to fail when reading the drive
                drives.append(letter + ':\\') 
            bitmask >>= 1

    return drives
