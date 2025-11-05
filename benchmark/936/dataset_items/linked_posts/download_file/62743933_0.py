def download(url: str, file_path='', attempts=2):
    """Downloads a URL content into a file (with large file support by streaming)

    :param url: URL to download
    :param file_path: Local file name to contain the data downloaded
    :param attempts: Number of attempts
    :return: New file path. Empty string if the download failed
    """
    if not file_path:
        file_path = os.path.realpath(os.path.basename(url))
    logger.info(f'Downloading {url} content to {file_path}')
    url_sections = urlparse(url)
    if not url_sections.scheme:
        logger.debug('The given url is missing a scheme. Adding http scheme')
        url = f'http://{url}'
        logger.debug(f'New url: {url}')
    for attempt in range(1, attempts+1):
        try:
            if attempt > 1:
                time.sleep(10)  # 10 seconds wait time between downloads
            with requests.get(url, stream=True) as response:
                response.raise_for_status()
                with open(file_path, 'wb') as out_file:
                    for chunk in response.iter_content(chunk_size=1024*1024):  # 1MB chunks
                        out_file.write(chunk)
                logger.info('Download finished successfully')
                return file_path
        except Exception as ex:
            logger.error(f'Attempt #{attempt} failed with error: {ex}')
    return ''
