from typing import Optional
import requests
# Test no parameters added
# def download_file(url):
# def download_file(url, local_filename):
# def download_file(url, chunk_size=None):
def download_file(url: str, local_filename: str, chunk_size: Optional[int] = None) -> str:
    # borrowed from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    # NOTE the stream=True parameter below
    # local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            # Test hardcoded value
            # for chunk in r.iter_content(chunk_size=8192): 
            for chunk in r.iter_content(chunk_size=chunk_size):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename

