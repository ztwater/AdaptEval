wget --save-cookies cookies.txt 'https://docs.google.com/uc?export=download&id=YOUR_FILE_ID' -O- | sed -rn 's/.*name="uuid" value=\"([0-9A-Za-z_\-]+).*/\1/p' > google_uuid.txt

wget --load-cookies cookies.txt -O YOUR_FILE_NAME 'https://drive.usercontent.google.com/download?export=download&id=YOUR_FILE_ID&confirm=t&uuid='$(<google_uuid.txt)
