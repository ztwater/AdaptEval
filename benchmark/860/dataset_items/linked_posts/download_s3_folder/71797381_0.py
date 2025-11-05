from sre_constants import SUCCESS
import boto3 
from os import path, makedirs 
from botocore.exceptions import ClientError
from boto3.exceptions import S3TransferFailedError

def download_s3_folder(s3_folder, local_dir, aws_access_key_id, aws_secret_access_key, aws_bucket, debug_en, datatype):
""""" Download the contents of a folder directory into a local area """""

success = True
# Start do processo de copia
print('[INFO] Downloading %s from bucket %s...' % (s3_folder, aws_bucket))

# Metodo que lista todos os objetos do Bucket. 
def get_all_s3_objects(s3, **base_kwargs):
    continuation_token = None
    while True:
        list_kwargs = dict(MaxKeys=1000, **base_kwargs)
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token
        response = s3.list_objects_v2(**list_kwargs)
        yield from response.get('Contents', [])
        if not response.get('IsTruncated'):
            break
        continuation_token = response.get('NextContinuationToken')

s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key)

all_s3_objects_gen = get_all_s3_objects(s3_client, Bucket=aws_bucket)

# Loop into os objetos do S3,
for obj in all_s3_objects_gen:
    source = obj['Key']
    if source.startswith(s3_folder):
        # Transform path to using fo SO
        destination = path.join(local_dir,source).replace('/','\\')
        
        if not path.exists(path.dirname(destination)):
            makedirs(path.dirname(destination))
        try:
            #print('copy')
            if destination.endswith(datatype):
                #print(destination)
                print('Copia do arquivo "%s" Sucesso' % (destination))
                s3_client.download_file(aws_bucket, source, destination)
        except (ClientError, S3TransferFailedError) as e:
            print('[ERROR] Could not download file "%s": %s' % (source, e))
            success = False
        if debug_en:
            print(f"[DEBUG] Downloading: {source} --> {destination}")

return success
