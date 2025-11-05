import requests as req

remote_url = 'http://www.example.com/sound.mp3'
local_file_name = 'sound.mp3'

data = req.get(remote_url)

# Save file data to local copy
with open(local_file_name, 'wb')as file:
    file.write(data.content)
