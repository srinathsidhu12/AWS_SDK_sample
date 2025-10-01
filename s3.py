import boto3

client = boto3.client('s3')

"""
#create_S3_bucket
response = client.create_bucket(
    ACL='private',
    Bucket='mysamplenew123',
    CreateBucketConfiguration={
       'LocationConstraint': 'ap-south-1'
    }
)
"""


"""
#upload file
s3 = boto3.client('s3')
s3.upload_file('./hello.txt', 'mysamplenew123', 'hello.txt')
print("File uploaded successfully!")
"""


"""
#list bucket objects
response = client.list_objects(
    Bucket='mysamplenew123',
)
"""



"""
#list buckets
response = client.list_buckets(
    MaxBuckets=1,
    #ContinuationToken='string',
    #Prefix='string',
    BucketRegion='ap-south-1'
)
"""

"""
#delete objects
response = client.delete_object(
    Bucket='mysamplenew123',
    Key='hello.txt',
)
"""


#delete bucket
response = client.delete_bucket(
    Bucket='mysamplenew123',
)



print(response)
