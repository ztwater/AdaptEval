import urllib.request
url_request = urllib.request.Request(url, headers=headers)
url_connect = urllib.request.urlopen(url_request)

#remember to open file in bytes mode
with open(filename, 'wb') as f:
    while True:
        buffer = url_connect.read(buffer_size)
        if not buffer: break

        #an integer value of size of written data
        data_wrote = f.write(buffer)

#you could probably use with-open-as manner
url_connect.close()
