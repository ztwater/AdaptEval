import unittest
from unittest.mock import patch, MagicMock
from s3_client import S3Client
import re, inspect

class TestDownloadS3Folder(unittest.TestCase):
    def test_download_s3_folder_success(self):
        class BucketObject():
            def __init__(self, key):
                self.key = key
        
        bucket_obj1 = BucketObject('s3_folder/subfolder/file1')
        bucket_obj2 = BucketObject('s3_folder/subfolder/file2')

        with patch('s3_client.S3Client') as mock:
            instance = mock.return_value
            instance.bucket.objects.filter.return_value = [bucket_obj1, bucket_obj2]
            instance.bucket.download_file = MagicMock()
            S3Client.download_s3_folder(instance, "s3_folder", "./test_dir")
            instance.bucket.download_file.assert_called()

    def test_download_s3_folder_return_none(self):
        with patch('s3_client.S3Client') as mock:
            instance = mock.return_value
            instance.bucket.objects.filter.return_value = []
            result = S3Client.download_s3_folder(instance, "s3_folder", "./test_dir")
            self.assertIsNone(result)

    def test_download_s3_folder_exception(self):
        with patch('s3_client.S3Client') as mock:
            instance = mock.return_value
            instance.bucket.objects.filter.side_effect = Exception("ClientError")
            with self.assertRaises(Exception) as result:
                S3Client.download_s3_folder(instance, "s3_folder", "./test_dir")
            self.assertTrue('ClientError' in str(result.exception))

    def test_string_updates(self):
        source = inspect.getsource(S3Client.download_s3_folder)
        pattern = r'\bbucket\s*=\s*s3\.Bucket\(\s*([^,\)]+)\s*\)'
        matched_old = re.search(pattern, source, re.MULTILINE | re.DOTALL)
        self.assertIsNone(matched_old)
        matched_new = re.search(r'self\.bucket\b', source)
        self.assertIsNotNone(matched_new)


if __name__ == '__main__':
    unittest.main()
