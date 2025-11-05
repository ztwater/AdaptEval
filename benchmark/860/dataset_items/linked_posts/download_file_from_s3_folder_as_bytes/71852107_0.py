import boto3
import tensorflow as tf

credentials = boto3.Session(botocore_session=boto3.setup_default_session(), 
                                region_name="us-east-1").get_credentials()
    

s3 = boto3.Session(aws_access_key_id=credentials.access_key,
                      aws_secret_access_key=credentials.secret_key).client('s3') 

#file_on_s3 : 's3://mybucket/data/sample.jpg'
bucket_name = 'mybucket'
file_key = 'data/sample.jpg'


file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)

# reading the file content in bytes
file_content = file_obj["Body"].read()  


img =  tf.io.decode_image(tf.convert_to_tensor(file_content, dtype=tf.string), 
                                channels=3, 
                                dtype=tf.dtypes.uint8, 
                                name=None, 
                                expand_animations=False)

img = tf.cast(img, tf.float32)
img_array = tf.image.resize(img, 
                            size=(224, 224),
                            method=tf.image.ResizeMethod.NEAREST_NEIGHBOR) 
