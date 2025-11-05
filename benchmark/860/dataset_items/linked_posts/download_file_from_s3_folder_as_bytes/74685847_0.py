img="https://{bucket}.s3.amazonaws.com/{folder}/"
context = ssl._create_unverified_context()
for i in range(1100,1102):
    image_url=img+str(i)+".png"
    im = Image.open(urllib.request.urlopen(image_url,context=context))
    im.show()`
