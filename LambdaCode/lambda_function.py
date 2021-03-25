import boto3

def lambda_handler(context, event):
    dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
    
    table = dynamodb.create_table(
        TableName='bruno_test_table_phonebook',
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'Name',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'Name',
                'AttributeType': 'S'
            },
    
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    
    return ("Table status:", table.table_status)  