def download_file(var_0):
    var_1 = var_0.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(var_0, stream=True) as r:
        r.raise_for_status()
        with open(var_1, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return var_1
