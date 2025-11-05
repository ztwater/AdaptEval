from tensorflow import keras

path_to_downloaded_file = keras.utils.get_file(
    fname="file name",
    origin="https://www.linktofile.com/link/to/file",
    extract=True,
    archive_format="zip",  # downloaded file format
    cache_dir="/",  # cache and extract in current directory
)
