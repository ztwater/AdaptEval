from cloudpathlib import CloudPath

cp = CloudPath("s3://bucket/folder/folder2/")
cp.download_to("local_folder")

