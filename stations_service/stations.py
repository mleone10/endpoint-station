#!/usr/bin/env python3

import json

def get(event, context):
    response = {
        "statusCode": 200,
        "body": "Hello there!"
    }

    return response

