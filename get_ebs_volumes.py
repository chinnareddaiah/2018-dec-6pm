import boto3
client = boto3.client('ec2')

resp = client.describe_instances()
snapshot_ids = []
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance id -- {instance['InstanceId']}")
        for block_dev in instance['BlockDeviceMappings']:
            print("------->  "+block_dev['Ebs']['VolumeId'])
            snapshot = client.create_snapshot(
                Description = 'boto3-demo-6pm',
                VolumeId = block_dev['Ebs']['VolumeId']
            )

            snapshot_ids.append(snapshot['SnapshotId'])

# Wait for snapshots to be availabile
print('Snapshots creation started')
waiter = client.get_waiter('snapshot_completed')
waiter.wait(
    SnapshotIds = snapshot_ids
)
print('Snapshots are completed')

# Copy snapshots to singapore region
client = boto3.client('ec2','ap-southeast-1')
for snapshot_id in snapshot_ids:
    client.copy_snapshot(
        SourceRegion='ap-south-1',
        SourceSnapshotId=snapshot_id,
        Description='boto3-demo-6pm'
    )