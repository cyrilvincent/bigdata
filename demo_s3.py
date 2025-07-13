import io
import boto3
from botocore.client import Config
import csv


s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'  # valeur fictive, requise par boto3
)

response = s3.list_objects_v2(Bucket='house')
for obj in response.get('Contents', []):
    print(obj['Key'])


response = s3.get_object(Bucket="house", Key="house.csv")
body = response['Body']
csv_content = csv.reader(io.TextIOWrapper(body, encoding='utf-8'))
for row in csv_content:
    print(row)
