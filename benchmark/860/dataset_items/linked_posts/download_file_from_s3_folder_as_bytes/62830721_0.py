import boto3
import io
from matplotlib import pyplot as plt

client = boto3.client("s3")

bucket='my_bucket'
key= 'my_key'

outfile = io.BytesIO()
client.download_fileobj(bucket, key, outfile)
outfile.seek(0)
img = plt.imread(outfile)

plt.imshow(img)
plt.show()
