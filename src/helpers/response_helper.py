import datetime
import bson.objectid
import json
from flask import Response

def bson_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    elif isinstance(x, datetime.date):
        return x.isoformat()
    elif isinstance(x, bson.objectid.ObjectId):
        return str(x)
    else:
        raise TypeError(x)

def format_response(code=200, data=None, message="Success response."):

    return_data = {
        'status': True,
        'message': message
    }

    if data:
        return_data['data'] = data

    json_result = json.dumps(return_data, default=bson_handler)
    return Response(json_result, content_type='application/json', status=code)


def format_error_response(code=500, message="Internal Server Error", data=None):

    return_data = {
        'status': False,
        'message': message
    }

    if data:
        return_data['error'] = data

    json_result = json.dumps(return_data, default=bson_handler)
    return Response(json_result, content_type='application/json', status=code)
