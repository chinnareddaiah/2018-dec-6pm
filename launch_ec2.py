'''
 Launch EC2 using Boto3
'''

import boto3
client = boto3.client('ec2')
client.run_instances(
    ImageId = 'ami-06bcd1131b2f55803',
    InstanceType = 't2.micro',
    MaxCount =1,
    MinCount = 1
)
