from __future__ import division
import boto3
import os

client = boto3.client('s3', aws_access_key_id=os.environ['AWS_SECRET_KEY'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name = os.environ['AWS_REGION'])

response = client.list_buckets()


def get_size(bucket_name):
    size = 0
    res = boto3.resource('s3', aws_access_key_id=os.environ['AWS_SECRET_KEY'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name= os.environ['AWS_REGION'])
    data = res.Bucket(bucket_name)
    for obj in data.objects.all():
        size += obj.size
    print("The Bucket '{}' in {} region, occupies '{}' bytes or '{}' MB.".format(bucket_name,os.environ['AWS_REGION'],size, size/(1024*1024)))

for rec in response['Buckets']:
    get_size(rec['Name'])
