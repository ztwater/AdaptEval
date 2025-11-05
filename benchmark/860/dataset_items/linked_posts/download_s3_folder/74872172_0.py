import boto3
import os
import shutil

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
)


def download_directory(bucket_name, s3_folder_name):
    s3_resource = session.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    objs = list(bucket.objects.filter(Prefix=s3_folder_name))
    for obj in objs:
        print("Try to Downloading " + obj.key)
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        out_name = obj.key.split('/')[-1]
        if out_name[-4:] == ".csv":
            bucket.download_file(obj.key, out_name)
            print(f"Downloaded {out_name}")
            dest_path = ('/').join(obj.key.split('/')[0:-1])
            shutil.move(out_name, dest_path)
            print(f"Moved File to {dest_path}")
        else:
            print(f"Skipping {out_name}")


download_directory("mybucket", "myfolder")
