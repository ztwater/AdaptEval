import urllib.request
with urllib.request.urlopen('http://www.example.com/') as f:
    html = f.read().decode('utf-8')
