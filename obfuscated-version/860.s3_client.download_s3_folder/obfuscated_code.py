import boto3
import os
var_0 = boto3.resource('s3') # assumes credentials & configuration are handled outside python in .aws directory or environment variables

def download_s3_folder(var_1, var_2, var_3=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    var_4 = var_0.Bucket(var_1)
    for obj in var_4.objects.filter(Prefix=var_2):
        var_5 = obj.key if var_3 is None else os.path.join(var_3, os.path.relpath(obj.key, var_2))
        if not os.path.exists(os.path.dirname(var_5)):
            os.makedirs(os.path.dirname(var_5))
        if obj.key[-1] == '/':
            continue
        var_4.download_file(obj.key, var_5)
