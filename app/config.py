import os

AWS_REGION = os.getenv("AWS_REGION", "eu-west-1")
TABLE_NAME = os.getenv("DDB_TABLE", "devops-challenge")
CODE_NAME = os.getenv("CODE_NAME", "theDoctor")
