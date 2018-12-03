import boto3
resource = boto3.resource('ec2')
resource.instances.filter(Filters=[
{
    'Name':'instance-state-name',
    'Values':['running']
}
]).stop()