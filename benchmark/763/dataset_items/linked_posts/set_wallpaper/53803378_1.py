def getWallpaper():
    sbuf = ctypes.create_string_buffer(512) # ctypes.c_buffer(512)
    ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_GETDESKWALLPAPER,len(sbuf),sbuf,0)
    return sbuf.value

def setWallpaper(path):
    changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
    ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER,0,path.encode(),changed) # "".encode() = b""
