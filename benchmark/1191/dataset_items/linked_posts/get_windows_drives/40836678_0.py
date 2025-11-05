>>> from string import ascii_uppercase
>>> reverse_alphabet = ascii_uppercase[::-1]
>>> from ctypes import windll # Windows only
>>> GLD = windll.kernel32.GetLogicalDisk
>>> drives = ['%s:/'%reverse_alphabet[i] for i,v in enumerate(bin(GLD())[2:]) if v=='1']
