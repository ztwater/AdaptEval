import googleapiclient.discovery
import oauth2client.client
from google.colab import auth
auth.authenticate_user()

def download_gdrive(id):
  creds = oauth2client.client.GoogleCredentials.get_application_default()
  service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)
  return service.files().get_media(fileId=id).execute()

a = download_gdrive("1F-yaQB8fdsfsdafm2l8WFjhEiYSHZrCcr")
