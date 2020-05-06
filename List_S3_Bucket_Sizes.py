from __future__ import division
import boto3
import os

session = boto3.Session(profile_name='default')
client = boto3.client('s3')

response = client.list_buckets()


def get_size(bucket_name):
    size = 0
    res = boto3.resource('s3')
    data = res.Bucket(bucket_name)
    for obj in data.objects.all():
        size += obj.size
    print("The Bucket '{}' in {} region, occupies '{}' bytes or '{}' MB.".format(bucket_name, session.region_name, size, size/(1024*1024)))



for rec in response['Buckets']:
    get_size(rec['Name'])
