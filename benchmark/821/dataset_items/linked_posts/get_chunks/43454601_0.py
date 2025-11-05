def make_chunks(data, chunk_size): 
    while data:
        chunk, data = data[:chunk_size], data[chunk_size:]
        yield chunk

>>> for chunk in make_chunks([1, 2, 3, 4, 5, 6, 7], 2):
...     print chunk
... 
[1, 2]
[3, 4]
[5, 6]
[7]
>>> 
