from ctypes import byref, create_unicode_buffer, sizeof, WinDLL
from ctypes.wintypes import DWORD, HMODULE, MAX_PATH

Psapi = WinDLL('Psapi.dll')
Kernel32 = WinDLL('kernel32.dll')

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

LIST_MODULES_ALL = 0x03

def EnumProcesses():
    buf_count = 256
    while True:
        buf = (DWORD * buf_count)()
        buf_size = sizeof(buf)
        res_size = DWORD()
        if not Psapi.EnumProcesses(byref(buf), buf_size, byref(res_size)):
            raise OSError('EnumProcesses failed')
        if res_size.value >= buf_size:
            buf_count *= 2
            continue
        count = res_size.value // (buf_size // buf_count)
        return buf[:count]

def EnumProcessModulesEx(hProcess):
    buf_count = 256
    while True:
        buf = (HMODULE * buf_count)()
        buf_size = sizeof(buf)
        needed = DWORD()
        if not Psapi.EnumProcessModulesEx(hProcess, byref(buf), buf_size,
                                          byref(needed), LIST_MODULES_ALL):
            raise OSError('EnumProcessModulesEx failed')
        if buf_size < needed.value:
            buf_count = needed.value // (buf_size // buf_count)
            continue
        count = needed.value // (buf_size // buf_count)
        return map(HMODULE, buf[:count])

def GetModuleFileNameEx(hProcess, hModule):
    buf = create_unicode_buffer(MAX_PATH)
    nSize = DWORD()
    if not Psapi.GetModuleFileNameExW(hProcess, hModule,
                                      byref(buf), byref(nSize)):
        raise OSError('GetModuleFileNameEx failed')
    return buf.value

def get_process_modules(pid):
    hProcess = Kernel32.OpenProcess(
        PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,
        False, pid)
    if not hProcess:
        raise OSError('Could not open PID %s' % pid)
    try:
        return [
            GetModuleFileNameEx(hProcess, hModule)
            for hModule in EnumProcessModulesEx(hProcess)]
    finally:
        Kernel32.CloseHandle(hProcess)

for pid in EnumProcesses():
    try:
        dll_list = get_process_modules(pid)
        print('dll_list: ', dll_list)
    except OSError as ose:
        print(str(ose))
    print('-' * 14)
