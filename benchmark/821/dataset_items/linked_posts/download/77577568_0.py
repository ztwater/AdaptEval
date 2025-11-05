import urllib3

resp = urllib3.request('GET', 'http://www.example.com/sound.mp3', preload_content=False, headers={'User-Agent': 'Customer User Agent If Needed'})

with open('sound.mp3', 'wb') as f:
    for chunk in resp.stream(65536):
        f.write(chunk)

resp.release_conn()
