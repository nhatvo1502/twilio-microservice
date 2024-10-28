import json
import os
from twilio.rest import Client

def lambda_handler(event, context):
    result = 'result'
    version = 'v1'
    account_sid = os.environ.get('account_sid')
    auth_token = os.environ.get('auth_token')
	twilio_number = os.environ.get('twilio_number')
    _body = event.get('body', None)
    _to = event.get('to', None)
    if _body != None and _to != None:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=twilio_number,
            body=_body,
            to=_to
        )
        result = message.sid
    else:
        result = 'Missing message body or recipient number'
    return {
            'statusCode': 200,
            'body': result,
            'version': version
        }