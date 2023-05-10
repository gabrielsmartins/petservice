import boto3
from boto3 import dynamodb


class DynamoDbConnectionFactory:
    _dynamodb = None


    @staticmethod
    def create_connection():
        if not DynamoDbConnectionFactory._dynamodb:
            DynamoDbConnectionFactory._dynamodb = boto3.resource('dynamodb',
                                                                 endpoint_url="http://localhost:8000",
                                                                 region_name='sa-east-1')
        return DynamoDbConnectionFactory._dynamodb
