#!/bin/bash

QUEUE_NAME="MyTestQueue"

aws sqs create-queue \
  --queue-name $QUEUE_NAME \
  --attributes VisibilityTimeout=60

echo "Queue $QUEUE_NAME created successfully."
