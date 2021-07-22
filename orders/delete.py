import os
import boto3

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')

def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ORDERS'])

    #delete item
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    #response
    response = {
        "statusCode": 200
    }

    return response
