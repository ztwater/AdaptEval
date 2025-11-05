import requests
import tqdm
import io
 
def download_as_bytes_with_progress(url: str, name: str = None) -> bytes:
    # source: https://stackoverflow.com/questions/71459213/requests-tqdm-to-a-variable
    resp = requests.get(url, stream=True, allow_redirects=True)
    total = int(resp.headers.get('content-length', 0))
    bio = io.BytesIO()
    if name is None:
        name = url
    with tqdm.tqdm(
        desc=name,
        total=total,
        unit='b',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in resp.iter_content(chunk_size=65536):
            bar.update(len(chunk))
            bio.write(chunk)
    return bio.getvalue()
  