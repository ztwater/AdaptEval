# libraries import
import boto3
import pandas as pd

# configure aws on command line
# aws configure
# enter your access key, access secret and region in which you create your bucket
# You get your access key and access password from security credentials under the iam
# if its disabled delete the previous one and then create the new one

s3_obj = boto3.client("s3") # object for accessing s3

# Downloading file code
s3_obj.download_file(
    Filename="./local_file_name_which_you_download_from_s3.csv",
    Bucket="your_bucket_name",
    Key="file_in_s3_bucket.csv"
# )
df = pd.read_csv('./local_file_name_which_you_download_from_s3.csv')
df.head()

# Uploading file code
s3_obj.upload_file(
    Filename="./local_file_name_which_you_download_from_s3.csv",
    Bucket="your_bucket_name",
    Key="file_in_s3_bucket.csv"
)

s3_obj_file = s3_obj.get_object(Bucket='bucket_name', Key='file_in_s3_bucket')['Body'].read()
df_upload = pd.read_excel(s3_obj_file)
df_upload.head()
