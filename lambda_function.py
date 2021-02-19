import boto3


def lambda_handler(event, context):
    # event['context']['sub']
    # event['context']['http-method'] == 'GET'

    result['status'] = 200
    result['message'] = 'Hello world'
    return result
