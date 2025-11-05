from tqdm import tqdm
import requests

url = "http://download.thinkbroadband.com/10MB.zip"
response = requests.get(url, stream=True)

with open("10MB", "wb") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)
