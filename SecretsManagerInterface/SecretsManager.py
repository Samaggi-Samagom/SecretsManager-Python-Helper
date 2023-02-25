import boto3
import json


def get_secret(secret_name: str, region: str = "eu-west-2", secret_data_key: str = "secret"):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )

    secret = get_secret_value_response['SecretString']

    return json.loads(secret)[secret_data_key]
