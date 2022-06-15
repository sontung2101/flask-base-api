import datetime

from flask_restful import Resource

from helpers import exception
from helpers.exception import CustomJsonException


class Health(Resource):
    def get(self):
        # raise CustomJsonException('error')
        return {'timestamps': datetime.datetime.now()}
