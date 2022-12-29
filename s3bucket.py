import os

import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv()


class s3client:
    def __init__(self):
        """
        This function will initiate the s3 client
        """
        self.s3 = boto3.resource(
            service_name = 's3',
            region_name = os.getenv('AWS_REGION'),
            aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        )
    
    def upload_to_aws(self, local_file, bucket, s3_file):
        """
        This function will upload a file to an S3 bucket
        :param local_file: File to upload
        :param bucket: Bucket to upload to
        :param s3_file: S3 file name
        :return: True if file was uploaded, else False
        """
        try:
            self.s3.meta.client.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_from_aws(self, s3_file, bucket, local_file):
        """
        This function will download a file from an S3 bucket
        :param s3_file: S3 file name
        :param bucket: Bucket to download from
        :param local_file: File to download
        :return: True if file was downloaded, else False
        """
        try:
            self.s3.meta.client.download_file(bucket, s3_file, local_file)
            print("Download Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

if __name__ == "__main__":
    s3 = s3client()
    #upload to s3
    #s3.upload_to_aws('hello.txt', 'myalice', 'hello.txt')

    #download from s3
    s3.download_from_aws('hello.txt', 'myalice', 'hello_test.txt')
