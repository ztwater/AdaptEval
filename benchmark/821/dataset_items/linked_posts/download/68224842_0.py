>>> import urllib3
>>> http = urllib3.PoolManager()
>>> r = http.request('GET', 'your_url_goes_here')
>>> r.status
   200
>>> r.data
   *****Response Data****
