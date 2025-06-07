AWS SQS Project that demonstrates how to create an SQS queue, send a message, and receive/delete the message using the AWS CLI and a Python script (Boto3).

---

## ✅ Project Title: **Simple AWS SQS Messaging System**

### 🎯 Objective:

Create an AWS SQS standard queue, send messages into it, retrieve messages separately, and delete them using Python (Boto3) and AWS CLI.

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
├── receive_message.py
├── delete_message.py
├── delete_queue.sh
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

## ✉️ 3. Send Message

**`send_message.py`**

```python
import boto3

queue_name = "MyTestQueue"
sqs = boto3.client('sqs')

queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody="Hello from Cloudnautic SQS Project!"
)

print("✅ Message sent!")
print("🆔 Message ID:", response['MessageId'])
```

---

## 📥 4. Receive Message (Only)

**`receive_message.py`**

```python
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
```

---

## 🗑️ 5. Delete Message (Only)

**`delete_message.py`**

```python
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
```

---

**`delete_queue.sh`**

```bash
#!/bin/bash

QUEUE_NAME="MyTestQueue"

# Get queue URL
QUEUE_URL=$(aws sqs get-queue-url --queue-name "$QUEUE_NAME" --query 'QueueUrl' --output text)

# Delete the queue
aws sqs delete-queue --queue-url "$QUEUE_URL"

echo "🗑️ Queue $QUEUE_NAME deleted successfully."
```

## 🚀 How to Run

```bash
# Step 1: Create the Queue
bash create_queue.sh

# Step 2: Install Python packages
pip install -r requirements.txt

# Step 3: Send a message
python3 send_message.py

# Step 4: Receive a message
python3 receive_message.py

# Step 5: Delete the message
python3 delete_message.py

# Step 6: Delete the Queue
bash delete_queue.sh
```

---

## ✅ Expected Output

* Message sent with ID confirmation
* Message received with ReceiptHandle shown
* Message deleted after using stored ReceiptHandle

---

Let me know if you'd like to add visibility timeout handling, batch messaging, or Dead Letter Queue (DLQ) integration.
