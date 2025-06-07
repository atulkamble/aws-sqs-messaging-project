import boto3
import json

queue_name = "MyTestQueue"
sqs = boto3.client('sqs')

queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=5
)

messages = response.get('Messages', [])
if not messages:
    print("📭 No messages in queue.")
else:
    for msg in messages:
        print("📨 Received:", msg['Body'])
        print("🧾 ReceiptHandle:", msg['ReceiptHandle'])

        # Save receipt handle to file for deletion step
        with open('last_receipt_handle.json', 'w') as f:
            json.dump({'ReceiptHandle': msg['ReceiptHandle']}, f)
