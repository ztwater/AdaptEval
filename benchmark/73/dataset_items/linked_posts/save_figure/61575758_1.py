import requests
from tqdm.auto import tqdm

eg_link = "https://github.com/tqdm/tqdm/releases/download/v4.46.0/tqdm-4.46.0-py2.py3-none-any.whl"
eg_file = eg_link.split('/')[-1]
response = requests.get(eg_link, stream=True)
with tqdm.wrapattr(open(eg_file, "wb"), "write", miniters=1,
                   total=int(response.headers.get('content-length', 0)),
                   desc=eg_file) as fout:
    for chunk in response.iter_content(chunk_size=4096):
        fout.write(chunk)
