#!/usr/bin/env python3

import json
import jwt

def get(event, context):
    headerPrefix = 'Bearer '
    username = str()

    authHeader = event.get('headers', {}).get('Authorization', {})

    if authHeader is not None:
        idToken = authHeader[len(headerPrefix):]
        username = jwt.decode(idToken, verify=False).get('cognito:username')

    response = {
        "statusCode": 200,
        "body": username
    }

    return response

