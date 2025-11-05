>>> import ctypes
>>> buff_size = ctypes.windll.kernel32.GetLogicalDriveStringsW(0,None)
>>> buff = ctypes.create_string_buffer(buff_size*2)
>>> ctypes.windll.kernel32.GetLogicalDriveStringsW(buff_size,buff)
8
>>> filter(None, buff.raw.decode('utf-16-le').split(u'\0'))
[u'C:\\', u'D:\\']
