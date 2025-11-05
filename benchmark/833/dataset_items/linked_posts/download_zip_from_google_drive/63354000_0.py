 SHAREABLE_LINK=<google drive shareable link>
 curl -L https://drive.google.com/uc\?id\=$(echo $SHAREABLE_LINK | cut -f6 -d"/")
