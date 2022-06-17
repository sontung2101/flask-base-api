import mongoengine as me
from helpers.models import BaseDocument


class Students(BaseDocument):
    student_no = me.StringField(required=True, unique=True)
    name = me.StringField(required=True, max_length=30)
    img_url = me.StringField(required=True, max_length=30)
    email = me.EmailField(equired=True, max_length=30)
