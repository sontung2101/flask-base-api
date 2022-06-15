from marshmallow import Schema, fields, ValidationError, pre_load, RAISE, validate


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")


class TrimmedString(fields.String):
    def _deserialize(self, value, *args, **kwargs):
        if hasattr(value, 'strip'):
            value = value.strip()
        return super()._deserialize(value, *args, **kwargs)


class StudentsSchema(Schema):
    student_id = fields.String(required=True, allow_none=False, validate=validate.Length(min=1))
    name = TrimmedString(required=True, allow_none=False, validate=validate.Length(min=1))
    email = fields.Email()
    img_url = fields.Str()

    class Meta:
        fields = ("student_id", "name", "img_url", "email")
        ordered = True

    @pre_load
    def check(self, data, **kwargs):
        pass
        return data
