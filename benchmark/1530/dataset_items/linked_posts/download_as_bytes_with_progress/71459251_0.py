import requests
import tqdm
import io

def download(url: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with tqdm.tqdm(
        desc=url,
        total=total,
        unit='b',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in resp.iter_content(chunk_size=65536):
            bar.update(len(chunk))
            yield chunk

bio = io.BytesIO()

for chunk in download('http://...'):
    # Do something with the chunk; this just stores it in memory.
    bio.write(chunk)

content = bio.getvalue()  # Get the contents of the BytesIO() as a bytes.
