import boto3
import os 

# set aws credentials 
s3r = boto3.resource('s3', aws_access_key_id='xxxxxxxxxxxxxxxxx',
    aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
bucket = s3r.Bucket('bucket_name')

# downloading folder 
prefix = 'dirname'
for object in bucket.objects.filter(Prefix = 'dirname'):
    if object.key == prefix:
        os.makedirs(os.path.dirname(object.key), exist_ok=True)
        continue;
    bucket.download_file(object.key, object.key)
