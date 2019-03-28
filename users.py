#!/usr/bin/env python3

import json
import requests

def login(event, context):
    body = {
            "loginLink": "https://auth.marioleone.me/login?response_type=code&client_id=7v7m04flk64gjrpqs7rqfm4agg&redirect_uri=https://endpointstation.marioleone.me/authenticate"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def authenticate(event, context):
    authCode = event.get("queryStringParameters", {}).get("code")
    body = {}

    if authCode is not None:
        tokenUrl = "https://auth.marioleone.me/oauth2/token"
        headers = {
                "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
                "client_id": "7v7m04flk64gjrpqs7rqfm4agg",
                "redirect_uri": "https://endpointstation.marioleone.me/authenticate",
                "grant_type": "authorization_code",
                "code": authCode
        }

        r = requests.post(tokenUrl, data=payload, headers=headers)

        body["jwt"] = r.json()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
