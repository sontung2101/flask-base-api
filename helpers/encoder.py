import datetime
import json

from flask import make_response


class Response(object):
    status_code: int = 200
    data: any = None
    error: any = None

    def __init__(self, status_code=200, data=None, error=None):
        self.status_code = status_code
        self.data = data
        self.error = error


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def encoder_response(data, code, headers=None):
    data = json.loads(json.dumps(data, cls=CustomEncoder))
    res = Response(code, data if str(code).startswith('2') else None, data if not str(code).startswith('2') else None)
    resp = make_response(res.__dict__, code)
    resp.headers.extend(headers or {})
    return resp
