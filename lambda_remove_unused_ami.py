import json
import boto3
client = boto3.client('ec2')
def lambda_handler(event, context):
   resp =  client.describe_images(
            Owners=['111111111111']
        )
   custom_amis = []
   for image in resp['Images']:
        custom_amis.append(image['ImageId'])
   used_amis = get_amis_in_use()

   for ami in custom_amis:
       if ami not in used_amis:
           client.deregister_image(ImageId=ami)
   return str(custom_amis)

def get_amis_in_use():
    used_amis = []
    resp = client.describe_instances()
    for reservation in resp['Reservations']:
        for instance in reservation['Instances']:
            used_amis.append(instance['ImageId'])

    return used_amis
