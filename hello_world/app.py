import json
import boto3
# import requests

#dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
