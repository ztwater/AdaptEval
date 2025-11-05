import sys

if 'ipykernel' in sys.modules:
    ip = sys.modules['ipykernel']
    ip_version = ip.version_info
    ip_client = ip.write_connection_file.__module__.split('.')[0]

# and this might be useful too:

ip_version = IPython.utils.sysinfo.get_sys_info()['ipython_version']
