from parallel_sync import wget
urls = ['http://something.png', 'http://somthing.tar.gz', 'http://somthing.zip']
wget.download('/tmp', urls)
# or a single file:
wget.download('/tmp', urls[0], filenames='x.zip', extract=True)
