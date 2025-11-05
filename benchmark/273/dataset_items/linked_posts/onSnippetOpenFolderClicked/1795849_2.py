if sys.platform=='win32':
    import _winreg
    path= r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon')
    for root in (_winreg.HKEY_CURRENT_USER, _winreg.HKEY_LOCAL_MACHINE):
        try:
            with _winreg.OpenKey(root, path) as k:
                value, regtype= _winreg.QueryValueEx(k, 'Shell')
        except WindowsError:
            pass
        else:
            if regtype in (_winreg.REG_SZ, _winreg.REG_EXPAND_SZ):
                shell= value
            break
    else:
        shell= 'Explorer.exe'
    subprocess.Popen([shell, d])
