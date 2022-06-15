from flask import jsonify
from helpers import codes as error_code, messages


class CustomJsonException(Exception):
    status_code = 400
    error = None
    data = None
    validates = {}

    def __init__(self, message=None, code=None, status_code=None, field=None):
        super().__init__()

        if not code and not message:
            code = error_code.UNEXPECTED_EXCEPTION

        if code:
            self.message = self.get_message(code)
            self.code = code

        if message:
            self.code = self.get_code(message)
            self.message = message

        if field:
            self.validates.update({
                field: {
                    'message': self.message,
                    'messageCode': self.code
                }
            })

        if status_code:
            self.status_code = status_code

        if isinstance(self.message, dict):
            for item_key, item_value in self.message.items():
                item_value = item_value[0] if isinstance(item_value, list) and len(item_value) > 0 else item_value
                self.validates.update({
                    item_key: {
                        'message': item_value,
                        'messageCode': self.get_code(item_value)
                    }
                })

        self.message = str(self.message)

        if self.validates:
            self.code = error_code.VALIDATION_ERROR
            self.message = self.get_message(self.code)

        self.error = {
            'message': self.message,
            'messageCode': self.code,
        }

        if self.validates:
            self.error.update({'validates': self.validates})

    @staticmethod
    def get_message(code=error_code.UNEXPECTED_EXCEPTION):
        return messages.ERROR_MESSAGE.get(code)

    @staticmethod
    def get_code(message='Unexpected Exception.'):
        for key, value in messages.ERROR_MESSAGE.items():
            if value == message:
                return key
        return error_code.UNEXPECTED_EXCEPTION

    def to_dict(self):
        rv = dict()

        rv['status_code'] = self.status_code
        rv['error'] = self.error
        rv['data'] = self.data
        return rv


def custom_json_exception(e):
    return jsonify(e.to_dict()), e.status_code
