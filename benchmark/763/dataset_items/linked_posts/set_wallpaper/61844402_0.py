import ctypes
ctypes.windll.user32.SystemParametersInfoW(20,0,"Path_wallpaper", 0) 
     speak("Background changed succesfully")
