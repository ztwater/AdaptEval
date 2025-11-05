AUTH="Authorization: Bearer the_access_token_goes_here"
FILEID="fileid_goes_here"
URL=https://www.googleapis.com/drive/v3/files/$FILEID?alt=media
curl --header "$AUTH" $URL >myfile.ext
