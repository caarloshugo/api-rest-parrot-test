import json
import os
import boto3

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_USERS'])
    
    #fetch all
    result = table.scan()

    #response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response
