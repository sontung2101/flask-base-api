import mongoengine as me


class Students(me.Document):
    student_id = me.StringField(required=True)
    name = me.StringField(required=True, max_length=30)
    img_url = me.StringField(required=True, max_length=30)
    email = me.EmailField(equired=True, max_length=30)
