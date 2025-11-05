# Importing [PyDrive][1] OAuth
from pydrive.auth import GoogleAuth

def download_tracking_file_by_id(file_id, download_dir):
    gauth = GoogleAuth(settings_file='../settings.yaml')
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("../credentials.json")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("../credentials.json")

    drive = GoogleDrive(gauth)

    logger.debug("Trying to download file_id " + str(file_id))
    file6 = drive.CreateFile({'id': file_id})
    file6.GetContentFile(download_dir+'mapmob.zip')
    zipfile.ZipFile(download_dir + 'test.zip').extractall(UNZIP_DIR)
    tracking_data_location = download_dir + 'test.json'
    return tracking_data_location
