 import os
 import subprocess

 remote_folder_name = 's3://my-bucket/my-dir'
 local_path = '.'
 if not os.path.exists(local_path):
     os.makedirs(local_path)
 subprocess.run(['aws', 's3', 'cp', remote_folder_name, local_path, '--recursive'])
