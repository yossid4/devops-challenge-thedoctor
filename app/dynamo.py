import boto3
from app import config

def get_secret():
    dynamodb = boto3.resource("dynamodb", region_name=config.AWS_REGION)
    table = dynamodb.Table(config.TABLE_NAME)
    response = table.get_item(Key={"codeName": config.CODE_NAME})
    return response["Item"]["secretCode"]
