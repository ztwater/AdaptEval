>>> import requests
>>> 
>>> url = "http://download.thinkbroadband.com/10MB.zip"
>>> r = requests.get(url)
>>> print len(r.content)
10485760
