import string
from ctypes import windll

def get_drives():
    var_0 = []
    var_1 = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if var_1 & 1:
            var_0.append(letter)
        var_1 >>= 1

    return var_0
