 import re
 import request
 from clint.textui import progress

 def get_filename(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0].replace('"', "")

def stream_download_file(url, output, chunk_size=1024, session=None, verbose=False):
    
    if session:
        file = session.get(url, stream=True)
    else:
        file = requests.get(url, stream=True)
        
    file_name = get_filename(file.headers.get('content-disposition'))
    filepath = "{}/{}".format(output, file_name)
    
    if verbose: 
        print ("Downloading {}".format(file_name))
        
    with open(filepath, 'wb') as f:
        total_length = int(file.headers.get('content-length'))
        for chunk in progress.bar(file.iter_content(chunk_size=chunk_size), expected_size=(total_length/chunk_size) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
    if verbose: 
        print ("Finished")
