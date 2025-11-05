from dlbar import DownloadBar

download_bar = DownloadBar()

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
