from win32com.client import GetObject
def get_proclist():
    WMI = GetObject('winmgmts:')
    processes = WMI.InstancesOf('Win32_Process')
    return [process.Properties_('ProcessID').Value for process in processes]
