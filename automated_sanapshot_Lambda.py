import boto3
import datetime

rds = boto3.client('rds')

def lambda_handler(event, context):
    snapshot_id = 'manual-snapshot-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier='my-db-instance'
    )
