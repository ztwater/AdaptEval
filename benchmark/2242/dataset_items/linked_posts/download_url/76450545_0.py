import requests
from tqdm import tqdm

     def DownloadFile(url):      
        req = requests.get(url, stream=True)
        total_length = int(req.headers.get('content-length'))
        chunk_size = 4194304 # 4Mb
        steps = total_length / chunk_size
        data = []
        for chunk in tqdm(req.iter_content(chunk_size=chunk_size), total=steps):
            text = chunk.decode("utf-8", "ignore") 
            for line in text.split("\n"):
                data.append(line.rstrip())
        return data 
