rm -rf /home/**********user***********/URLS_DECODED.txt
COUNTER=0
while read p; do 
    string=$p
    hash="${string#*id=}"
    hash="${hash%&*}"
    hash="${hash#*file/d/}"
    hash="${hash%/*}"
    let COUNTER=COUNTER+1
    echo "Enlace "$COUNTER" id="$hash
    URL_TO_DOWNLOAD=$(wget --spider --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id='$hash -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id="$hash 2>&1 | grep *******Localización***********: | head -c-13 | cut -c16-)
    rm -rf /tmp/cookies.txt
    echo -e "$URL_TO_DOWNLOAD\r" >> /home/**********user***********/URLS_DECODED.txt
    echo "Enlace "$COUNTER" URL="$URL_TO_DOWNLOAD
done < /home/**********user***********/URLS.txt
