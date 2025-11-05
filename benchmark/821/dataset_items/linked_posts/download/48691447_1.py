import urllib.request
import shutil

url = "http://www.somewebsite.com/something.pdf"
output_file = "save_this_name.pdf"
with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
