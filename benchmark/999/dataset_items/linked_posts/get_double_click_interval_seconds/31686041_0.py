get_double_click_time():
    """ Gets the Windows double click time in ms """
    from ctypes import windll
    return int(windll.user32.GetDoubleClickTime())
