import os
import json
import boto3

from orders import decimalencoder

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ORDERS'])

    #get item
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    #response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }

    return response
