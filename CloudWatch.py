import boto3
import time

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

def publish_custom_metric(name, value, namespace='MyApp'):
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': name,
                'Timestamp': time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                'Value': value,
                'Unit': 'Count'
            }
        ]
    )
