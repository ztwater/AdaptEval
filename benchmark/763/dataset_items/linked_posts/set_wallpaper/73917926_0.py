import ctypes
ctypes.windll.user32.SystemParametersInfoW(20,0,path:os.PathLike,3)
