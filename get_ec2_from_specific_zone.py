import boto3
client = boto3.client('ec2')
zone = input('Enter availability Zone')
resp = client.describe_instances(
    Filters = [
        {
            'Name':'availability-zone',
            'Values':[zone]
        }
    ]
)
print(resp['Reservations'])