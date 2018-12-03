"""
  Example two, Stop EC2 instances
"""

import boto3
client = boto3.client('ec2')
resp = client.stop_instances(
    InstanceIds=[
        'i-024164f8493fa21ad',
        'i-05900ed545d759a8c'
    ]
)

for instance in resp['StoppingInstances']:
    current_status = instance['CurrentState']['Name']
    previous_status = instance['PreviousState']['Name']
    id = instance['InstanceId']
    print(f"Instance with id {id}, previous state = {previous_status} and current status is {current_status} ")
