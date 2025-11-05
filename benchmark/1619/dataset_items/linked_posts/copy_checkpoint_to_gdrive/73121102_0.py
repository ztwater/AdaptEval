import shutil

compressed_file = shutil.make_archive(
        base_name='archive',   # archive file name w/o extension
        format='gztar',        # available formats: zip, gztar, bztar, xztar, tar
        root_dir='path/to/dir' # directory to compress
)
