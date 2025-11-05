import ctypes
FILE_ATTRIBUTE_HIDDEN = 0x02

ret = ctypes.windll.kernel32.SetFileAttributesW(ur'G:\Dir\folder1',
                                                FILE_ATTRIBUTE_HIDDEN)
if ret:
    print('attribute set to Hidden')
else:  # return code of zero indicates failure -- raise a Windows error
    raise ctypes.WinError()
