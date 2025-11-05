import psutil
drps = psutil.disk_partitions()
drives = [dp.device for dp in drps if dp.fstype == 'NTFS']
