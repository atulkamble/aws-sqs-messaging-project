import boto3
import json
import os

queue_name = "MyTestQueue"
sqs = boto3.client('sqs')

queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

# Read ReceiptHandle from file
if not os.path.exists('last_receipt_handle.json'):
    print("❌ No receipt handle found. Run receive_message.py first.")
    exit()

with open('last_receipt_handle.json') as f:
    receipt_data = json.load(f)

receipt_handle = receipt_data['ReceiptHandle']

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print("🗑️ Message deleted successfully.")
