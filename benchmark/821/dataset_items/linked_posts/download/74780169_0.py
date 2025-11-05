import os
import requests


outfile = os.path.join(SAVE_DIR, file_name)
response = requests.get(URL, stream=True)
with open(outfile,'wb') as output:
  output.write(response.content)
