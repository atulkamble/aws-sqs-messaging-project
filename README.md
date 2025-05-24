**AWS SQS Project** that demonstrates how to create an SQS queue, send a message, and receive/delete the message using the AWS CLI and a Python script (Boto3).

---

## ✅ Project Title: **Simple AWS SQS Messaging System**

### 🎯 Objective:

Create an AWS SQS standard queue, send messages into it, retrieve and delete those messages using a Python script.

---

## 🔧 Project Prerequisites:

1. **AWS CLI Installed & Configured**
2. **IAM User with `AmazonSQSFullAccess`**
3. **Python 3.x and Boto3 installed**

---

## 📁 Project Structure

```
sqs-project/
│
├── create_queue.sh
├── send_message.py
├── receive_delete_message.py
└── requirements.txt
```

---

## 🛠️ 1. Create Queue using AWS CLI

**`create_queue.sh`**

```bash
#!/bin/bash

QUEUE_NAME="MyTestQueue"

aws sqs create-queue \
  --queue-name $QUEUE_NAME \
  --attributes VisibilityTimeout=60

echo "Queue $QUEUE_NAME created successfully."
```

---

## 📦 2. Install Python Requirements

**`requirements.txt`**

```
boto3
```

```bash
pip install -r requirements.txt
```

---

## ✉️ 3. Send Message using Python

**`send_message.py`**

```python
import boto3

queue_name = "MyTestQueue"
sqs = boto3.client('sqs')

# Get queue URL
queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

# Send message
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody="Hello from Cloudnautic SQS Project!"
)

print("Message sent! Message ID:", response['MessageId'])
```

---

## 📥 4. Receive and Delete Message using Python

**`receive_delete_message.py`**

```python
import boto3

queue_name = "MyTestQueue"
sqs = boto3.client('sqs')

# Get queue URL
queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

# Receive message
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=5
)

messages = response.get('Messages', [])
if not messages:
    print("No messages in queue.")
else:
    for msg in messages:
        print("Received:", msg['Body'])

        # Delete message
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=msg['ReceiptHandle']
        )
        print("Message deleted.")
```

---

## 🚀 How to Run

```bash
# Step 1: Create Queue
bash create_queue.sh

# Step 2: Install Python packages
pip install -r requirements.txt

# Step 3: Send a message
python send_message.py

# Step 4: Receive and delete the message
python receive_delete_message.py
```

---

## ✅ Expected Output

* Message ID after sending
* Message content when received
* Confirmation of deletion

---
