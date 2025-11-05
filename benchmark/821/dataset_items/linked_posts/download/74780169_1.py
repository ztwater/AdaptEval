import os
import requests
import shutil
 
outfile = os.path.join(SAVE_DIR, file_name)
response = requests.get(url, stream = True)
with open(outfile, 'wb') as f:
  shutil.copyfileobj(response.content, f)
