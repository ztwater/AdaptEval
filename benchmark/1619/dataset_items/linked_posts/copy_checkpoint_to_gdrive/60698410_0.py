import traceback
import subprocess

try:
    cmd = ['tar', 'czfj', output_filename, file_to_archive]
    output = subprocess.check_output(cmd).decode("utf-8").strip() 
    print(output)          
except Exception:       
    print(f"E: {traceback.format_exc()}")       
