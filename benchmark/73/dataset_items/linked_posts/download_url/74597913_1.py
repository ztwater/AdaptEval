import time
import math
import requests
from tqdm import tqdm


def download_file(url, filename, update_interval=500, chunk_size=4096):
    def memory2str(mem):
        sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        power = int(math.log(mem, 1024))
        size = sizes[power]
        for _ in range(power):
            mem /= 1024
        if power > 0:
            return f'{mem:.2f}{size}'
        else:
            return f'{mem}{size}'
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')
        if total_length is None:
            f.write(response.content)
        else:
            print(f'Downloading {filename}.', flush=True)
            downloaded, total_length = 0, int(total_length)
            total_size = memory2str(total_length)
            bar_format = '{percentage:3.0f}%|{bar:20}| {desc} [{elapsed}<{remaining}' \
                         '{postfix}]'
            if update_interval * chunk_size * 100 >= total_length:
                update_interval = 1
            with tqdm(total=total_length, bar_format=bar_format) as bar:
                counter = 0
                now_time, now_size = time.time(), downloaded
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    downloaded += len(data)
                    counter += 1
                    bar.update(len(data))
                    if counter % update_interval == 0:
                        ellapsed = time.time() - now_time
                        runtime_downloaded = downloaded - now_size
                        now_time, now_size = time.time(), downloaded

                        cur_size = memory2str(downloaded)
                        speed_size = memory2str(runtime_downloaded / ellapsed)
                        bar.set_description(f'{cur_size}/{total_size}')
                        bar.set_postfix_str(f'{speed_size}/s')

                        counter = 0
