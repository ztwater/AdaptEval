import urllib
response = urllib.urlopen('http://www.example.com/sound.mp3')
mp3 = response.read()
