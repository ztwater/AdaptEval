import os
import boto3
from pathlib import Path

def download_s3_dir(bucketName, remote_dir, local_dir):
    assert remote_dir.endswith('/')
    assert local_dir.endswith('/')
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketName) 
    objs = bucket.objects.filter(Prefix=remote_dir)
    sorted_objs = sorted(objs, key=attrgetter("key"))
    for obj in sorted_objs:
        path = Path(os.path.dirname(local_dir + obj.key))
        path.mkdir(parents=True, exist_ok=True)
        if not obj.key.endswith("/"):
            bucket.download_file(obj.key, str(path) + "/" + os.path.split(obj.key)[1])
