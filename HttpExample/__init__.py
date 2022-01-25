import logging

import azure.functions as func

import json
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #HTTP url
    url = ""

    #HTTP header
    headers = {
        'Authorization': '',
        'Content-Type': 'text/plain'
        }

    #HTTP body
    body = dict()
    body['client_payload'] = req.get_json()
    json_body = (json.dumps(body)).encode('utf-8')
    
    requests.request("POST", url, headers=headers, data=json_body)

    return func.HttpResponse(
            status_code=200
        )
