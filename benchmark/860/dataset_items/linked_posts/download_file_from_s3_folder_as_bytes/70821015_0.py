import os
import boto3
from PIL import Image
import io

AWS_ACCESS_KEY_ID = 'your-aws-access-key'
AWS_SECRET_ACCESS_KEY = 'your-aws-secret'

s3 = boto3.resource('s3',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def image_from_s3(bucket, key):
    bucket = s3.Bucket(bucket)
    image = bucket.Object(key)
    img_data = image.get().get('Body').read()
    return Image.open(io.BytesIO(img_data))

# call the function
image_from_s3("your-aws-bucket-name", "file-path")

# example
image_from_s3("my-images", "profile/2022/123.png")
