from marshmallow import Schema, fields, ValidationError, pre_load, RAISE, validate, validates
from .models import Students


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
    id = fields.String()
    student_no = fields.String(required=True, allow_none=False, validate=validate.Length(min=1))
    name = TrimmedString(required=True, allow_none=False, validate=validate.Length(min=1))
    email = fields.Email(required=True, allow_none=False)
    img_url = TrimmedString(allow_none=False)
    updated_at = fields.DateTime()
    created_at = fields.DateTime()

    class Meta:
        fields = ("id", "student_no", "name", "img_url", "email", "updated_at", "created_at")
        ordered = True

    @validates('student_no')
    def no_duplicate_student_no(self, value):
        check_duplicate = Students.objects(student_no=value)
        if check_duplicate:
            raise ValidationError('duplicate')

    @pre_load
    def check(self, data, **kwargs):
        # this funtion to modify data input
        # TODO
        return data
