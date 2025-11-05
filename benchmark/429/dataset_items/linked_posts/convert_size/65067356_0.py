$ pip install -qqq datasize
$ python
...
>>> from datasize import DataSize
>>> 'My new {:GB} SSD really only stores {:.2GiB} of data.'.format(DataSize('750GB'),DataSize(DataSize('750GB') * 0.8))
'My new 750GB SSD really only stores 558.79GiB of data.'
