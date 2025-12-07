import boto3

queue_name = "MyTestQueue"
sqs = boto3.client('sqs')

# Get queue URL
queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

# Send message
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody="Hello from SQS Project!"
)

print("Message sent! Message ID:", response['MessageId'])
