import boto3
import os
from botocore.exceptions import ClientError
from logger import get_configured_logger


class S3Client(object):
    def __init__(self,bucket_name):
        """
        Credentials & configuration are handled in .aws directory or environment variables
        """
        self.s3r = boto3.resource('s3')
        self.logger = get_configured_logger(self.__class__.__name__)
        self.bucket = self.s3r.Bucket(bucket_name)

    def download_s3_folder(self, s3_folder, local_dir=None):
        """
        Download the contents of a S3 folder, with sub-directories
        ref: https://stackoverflow.com/a/62945526/11483674
        
        Args:
            bucket_name: the name of the s3 bucket
            s3_folder: the folder path in the s3 bucket
            local_dir: a relative or absolute directory path in the local file system
        """
        try:
            for obj in self.bucket.objects.filter(Prefix=s3_folder):
                target = obj.key if local_dir is None \
                    else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
                if not os.path.exists(os.path.dirname(target)):
                    os.makedirs(os.path.dirname(target))
                if obj.key[-1] == '/':
                    continue
                self.bucket.download_file(obj.key, target)
            return None
        except ClientError as e:
            self.logger.exception(e)
            return str(e)
