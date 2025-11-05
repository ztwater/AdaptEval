import ctypes
import os
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, 'C:\\Users\\godet\\OneDrive\\Images\\breaker_wall.jpg', 0)
