import boto3
client = boto3.client('ec2')
resp = client.describe_instances(
    Filters = [
        {
            'Name':'tag:Environment',
            'Values':['Dev']
        }
    ]
)
print(resp['Reservations'])