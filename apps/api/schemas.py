from marshmallow import Schema, fields, ValidationError, pre_load, RAISE, validate


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")


class StudentsSchema(Schema):
    student_id = fields.Str(required=True, allow_none=False)
    name = fields.Str(required=True, allow_none=False)
    email = fields.Email()
    img_url = fields.Str()

    class Meta:
        fields = ("student_id", "name", "img_url", "email")
        ordered = True

    @pre_load
    def check(self, data, **kwargs):
        pass
        return data
