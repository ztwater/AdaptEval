import requests
from tqdm import tqdm


def download(var_0: str, var_1: str):
    var_2 = requests.get(var_0, stream=True)
    var_3 = int(var_2.headers.get('content-length', 0))
    # Can also replace 'file' with a io.BytesIO object
    with open(var_1, 'wb') as file, tqdm(
        desc=var_1,
        var_3=var_3,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in var_2.iter_content(chunk_size=1024):
            var_4 = file.write(data)
            bar.update(var_4)
