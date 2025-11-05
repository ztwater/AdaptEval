import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import boto3
import tempfile

s3 = boto3.resource('s3', region_name='us-east-2')
bucket = s3.Bucket('sentinel-s2-l1c')
object = bucket.Object('tiles/10/S/DG/2015/12/7/0/B01.jp2')
tmp = tempfile.NamedTemporaryFile()

with open(tmp.name, 'wb') as f:
    object.download_fileobj(f)
    img=mpimg.imread(tmp.name)
    # ...Do jobs using img
