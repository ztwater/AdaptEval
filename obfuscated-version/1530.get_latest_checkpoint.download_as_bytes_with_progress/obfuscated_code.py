import requests
import tqdm
import io


def download_as_bytes_with_progress(var_0: str) -> bytes:
    var_1 = requests.get(var_0, stream=True)
    var_2 = int(var_1.headers.get('content-length', 0))
    var_3 = io.BytesIO()
    with tqdm.tqdm(
        desc=var_0,
        var_2=var_2,
        unit='b',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in var_1.iter_content(chunk_size=65536):
            bar.update(len(chunk))
            var_3.write(chunk)
    return var_3.getvalue()
