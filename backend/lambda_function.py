import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DATABASE_TABLE_NAME', 'visitor_counter')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    try:
        response = table.update_item(
            Key={'id': 'views'},
            UpdateExpression="ADD #c :val",
            ExpressionAttributeNames={'#c': 'count'},
            ExpressionAttributeValues={':val': 1},
            ReturnValues="UPDATED_NEW"
        )
        
        current_count = int(response['Attributes']['count'])
        
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({"count": current_count})
        }

    except ClientError as e:
        print(f"Database operation failed: {e.response['Error']['Message']}")
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"error": "Failed to update record sequence"})
        }