import json
import logging
import os
import time
import uuid
from datetime import datetime
import botocore
import boto3

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'email' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the item.")
    
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_USERS'])

    item = {
        'id': str(uuid.uuid1()),
        'email': data['email'],
        'name': data['name'],
        'createdAt': date_time,
        'updatedAt': date_time,
    }
    
    try:
        #put item
        table.put_item(Item=item, ConditionExpression='attribute_not_exists(email)')
        response = {
            "statusCode": 200,
            "body": json.dumps(item)
        }
    except botocore.exceptions.ClientError as e:
        #response
        response = {
            "statusCode": 400,
            "body": '{"error" : client already exists"}'
        }
        
    return response
