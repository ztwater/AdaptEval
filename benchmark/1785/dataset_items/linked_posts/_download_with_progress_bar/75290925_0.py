r = requests.get(url, stream=True)
progress_bar = tqdm(total=int(r.headers.get('content-length', 0)), unit='B', unit_scale=True, desc=url)
dat = b''.join(x for x in r.iter_content(chunk_size=16384) if progress_bar.update(len(x)) or True)
