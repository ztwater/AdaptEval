bitmask = (bin(windll.kernel32.GetLogicalDrives())[2:])[::-1]  # strip off leading 0b and reverse
drive_letters = [ascii_uppercase[i] + ':/' for i, v in enumerate(bitmask) if v == '1']
