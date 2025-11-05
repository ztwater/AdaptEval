from http import HTTPStatus, client
from shutil import copyfileobj

# using https
connection = client.HTTPSConnection("www.example.com")
with connection.request("GET", "/noise.mp3") as response:
    if response.status == HTTPStatus.OK:
        copyfileobj(response, open("noise.mp3")
    else:
        raise Exception("request needs work")
