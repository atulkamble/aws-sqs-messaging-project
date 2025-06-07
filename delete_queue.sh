#!/bin/bash

QUEUE_NAME="MyTestQueue"

# Get queue URL
QUEUE_URL=$(aws sqs get-queue-url --queue-name "$QUEUE_NAME" --query 'QueueUrl' --output text)

# Delete the queue
aws sqs delete-queue --queue-url "$QUEUE_URL"

echo "🗑️ Queue $QUEUE_NAME deleted successfully."
