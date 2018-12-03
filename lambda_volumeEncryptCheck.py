import json
import boto3
client = boto3.client('ec2')
sns = boto3.client('sns')
sns_arn = 'arn:aws:sns:ap-south-1:111111111111:compliancealerts'
def lambda_handler(event, context):
    response = client.describe_volumes(
        Filters = [
              {
                  'Name':'encrypted',
                  'Values':['false']
              }
            ]
        )
    vol_ids = []
    for vol in response['Volumes']:
        vol_ids.append(vol['VolumeId'])

    sns.publish(
        Subject='Alert- Unencrypted Volumes Found',
        Message = str(vol_ids),
        TopicArn = sns_arn
    )
    return str(vol_ids)
