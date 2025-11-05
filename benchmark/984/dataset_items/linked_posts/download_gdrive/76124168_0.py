import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.action = None

    def handle_starttag(self, tag, attrs):
        if tag == "form":
            for name, value in attrs:
                if name == "id" and value == "download-form":
                    for name, value in attrs:
                        if name == "action":
                            self.action = value

DOWNLOAD_URL = 'https://docs.google.com/uc?export=download'
session = requests.Session()
response = session.get(file_url, params={'id': id}, stream=True)

content_type = response.headers['content-type']
if content_type == 'text/html; charset=utf-8':
    parser = MyHTMLParser()
    parser.feed(response.text)
    download_url = parser.action
    response = session.post(download_url, stream=True)
    
file = response.content
