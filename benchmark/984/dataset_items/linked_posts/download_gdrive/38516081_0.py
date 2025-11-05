# Initialize GoogleDriveFile instance with file id.
file_obj = drive.CreateFile({'id': '<your file ID here>'})
file_obj.GetContentFile('cats.png') # Download file as 'cats.png'.
