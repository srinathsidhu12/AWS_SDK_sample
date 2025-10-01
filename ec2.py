import boto3

client = boto3.client('ec2')

#Creation of Ec2 instance
"""
response = client.run_instances(
    ImageId='ami-01b6d88af12965bb6',
    InstanceType='t2.micro',
    SecurityGroupIds=[
        'sg-0a80957311618ef73',
    ],
    MaxCount=1,
    MinCount=1,
    KeyName='sample',
    SubnetId='subnet-030893069bd3cf64d',
    DryRun=False
)
"""



#Stopping created instance
"""
response = client.stop_instances(
    InstanceIds=[
        'i-0e0f9963f97016423',
    ]
)
"""


"""
#Modifying instance type
response = client.modify_instance_attribute(
    InstanceId='i-0e0f9963f97016423',
    InstanceType={
        'Value': 't2.nano'
    }
)
"""

"""
#Starting the stopped instance
response = client.start_instances(
    InstanceIds=[
        'i-0e0f9963f97016423',
    ],
    DryRun=False
)
"""

"""
#creating_tags_for instance(Adds a tag in tags section of instance)
response = client.create_tags(
    DryRun=False,
    Resources=[
        'i-0e0f9963f97016423',
    ],
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
"""

"""
#Describing the instance
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:environment',
            'Values': [
                'dev',
            ]
        },
    ]
)
"""

"""
#creating_tags_for instance
response = client.create_tags(
    DryRun=False,
    Resources=[
        'i-0e0f9963f97016423',
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Myboto3instance'
        },
    ]
)
"""

#Terminating_Ec2_Instance
response = client.terminate_instances(
    DryRun=False,
    InstanceIds=[
        'i-0e0f9963f97016423',
    ]
)


print(response) 
