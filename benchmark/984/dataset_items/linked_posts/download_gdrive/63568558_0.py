from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io

credz = {} #put json credentials her from service account or the like
# More info: https://cloud.google.com/docs/authentication

credentials = service_account.Credentials.from_service_account_info(credz)
drive_service = build('drive', 'v3', credentials=credentials)

file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
request = drive_service.files().get_media(fileId=file_id)
#fh = io.BytesIO() # this can be used to keep in memory
fh = io.FileIO('file.tar.gz', 'wb') # this can be used to write to disk
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))


