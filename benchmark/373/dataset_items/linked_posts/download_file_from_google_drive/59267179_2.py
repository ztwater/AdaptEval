function wget_gdrive {

    GDRIVE_FILE_ID=$1
    DEST_PATH=$2

    wget --save-cookies cookies.txt 'https://docs.google.com/uc?export=download&id='$GDRIVE_FILE_ID -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt
    wget --load-cookies cookies.txt -O $DEST_PATH 'https://docs.google.com/uc?export=download&id='$GDRIVE_FILE_ID'&confirm='$(<confirm.txt)
    rm -fr cookies.txt confirm.txt
}
