import json
import os
import boto3

from orders import decimalencoder

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')

def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ORDERS'])

    #fetch all
    result = table.scan()

    #reponse
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
