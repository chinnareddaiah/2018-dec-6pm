import boto3
client = boto3.client('ec2')
ids = []
resp = client.describe_instances(
    Filters = [
        {
            'Name':'instance-state-name',
            'Values':['running']
        }
    ]
)
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        ids.append(instance['InstanceId'])

client.stop_instances(
    InstanceIds = ids
)
