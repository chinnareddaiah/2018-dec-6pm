import boto3
client = boto3.client('ec2')

resp = client.describe_instances(
    Filters = [
        {
            'Name':'instance-state-name',
            'Values':['running']
        }
    ]
)
print(resp['Reservations'])