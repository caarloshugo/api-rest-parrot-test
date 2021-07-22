import json
import time
import logging
import os
from datetime import datetime
from orders import decimalencoder
import boto3

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')

def update(event, context):
    data = json.loads(event['body'])
    if 'client' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the item.")
        return

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ORDERS'])

    #update item
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames = { "#total": "total" },
        ExpressionAttributeValues={
          ':client': data['client'],
          ':total': data['total'],
          ':products': data['products'],
          ':updatedAt': date_time,
        },
        UpdateExpression='SET client = :client, #total = :total, products = :products, updatedAt = :updatedAt',
        ReturnValues='UPDATED_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'], cls=decimalencoder.DecimalEncoder)
    }

    return response
