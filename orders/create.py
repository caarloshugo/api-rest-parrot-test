import json
import logging
import os
import time
import uuid
from datetime import datetime
import boto3

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if 'client' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the item.")
    
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ORDERS'])

    item = {
        'id': str(uuid.uuid1()),
        'user_email': event['requestContext']['authorizer']['user_email'],
        'client': data['client'],
        'total': data['total'],
        'products': data['products'],
        'createdAt': date_time,
        'updatedAt': date_time,
    }

    #put item
    table.put_item(Item=item)

    #response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
