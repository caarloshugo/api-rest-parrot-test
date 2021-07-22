import json
import os
import boto3
from boto3.dynamodb.conditions import Key

from orders import decimalencoder

if 'IS_OFFLINE' in os.environ:
	dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
	dynamodb = boto3.resource('dynamodb')

def report(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ORDERS'])

    #filterExpression
    if event['pathParameters']['start_date'] == event['pathParameters']['end_date']:
        filterExpression = Key('createdAt').begins_with(event['pathParameters']['start_date'])
    else:
        filterExpression = Key('createdAt').between(event['pathParameters']['start_date'],event['pathParameters']['end_date'])

    result = table.scan(ProjectionExpression='products', FilterExpression=filterExpression)

    #reponse
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
