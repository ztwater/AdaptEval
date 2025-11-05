function curl_gdrive {

    GDRIVE_FILE_ID=$1
    DEST_PATH=$2

    curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${GDRIVE_FILE_ID}" > /dev/null
    curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${GDRIVE_FILE_ID}" -o ${DEST_PATH}
    rm -f cookie
}
