import json
import boto3

#dynamodb = boto3.resource('dynamodb')
dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
table = dynamodb.Table('Test')

def lambda_handler(event, context):
    if not 'queryStringParameters' in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'queryStringParameters is required'})
        }

    # idを取得
    id = event['queryStringParameters']['id']
    if id is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'id is required'})
        }
        
    # DynamoDBからデータを取得    
    resp = table.get_item(Key={'id': id})
    if 'Item' not in resp:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'item not found'})
        }

    # レスポンスを作成
    item = resp['Item']['item']        
    return {
        'statusCode': 200,
        'body': json.dumps({'id': id, 'item': item})
    }