from flask_restful import reqparse, abort, Resource
from apps.api.models import Students
from helpers import codes
from helpers.exception import CustomJsonException
import uuid
from .schemas import StudentsSchema
from flask import request
from marshmallow import ValidationError


class StudentsList(Resource):
    def get(self):
        students = Students.objects().all()
        schema = StudentsSchema(many=True)
        result = schema.dump(students)
        if students:
            return result
        raise CustomJsonException(status_code=401)

    def post(self):
        try:
            random_id = str(uuid.uuid1())
            bttf = Students(student_id=random_id[:8], name=f"user_{random_id[:8]}",
                            img_url=f"image_url_{random_id[:8]}")
            bttf.save()
            return None
        except Exception as exc:
            raise CustomJsonException(message=exc, status_code=402)


class Student(Resource):

    def get(self, pk):
        try:
            student = Students.objects(student_id=pk).first()
        except Exception as exc:
            raise CustomJsonException(message=exc)
        schema = StudentsSchema()
        result = schema.dump(student)
        return result

    def post(self, pk):
        json_data = request.get_json()
        json_data["student_id"] = pk
        if not json_data:
            raise CustomJsonException(message="No input data provided", code=400)
        quote_schema = StudentsSchema()
        try:
            data = quote_schema.load(json_data)
        except ValidationError as err:
            raise CustomJsonException(message=err.messages, code=422)
        student = Students.objects(student_id=pk).first()

        if student is None:
            # Create a new student
            student = Students(student_id=pk, name=data["name"], img_url=data["img_url"], email=data["email"])
        else:
            # update a new student
            student.name = data["name"]
            student.img_url = data["img_url"]
            student.email = data["email"]
        student.save()
        result = quote_schema.dump(student)
        return result

    def delete(self, pk):
        student = Students.objects(student_id=pk).first()
        if student is not None:
            student.delete()
            return None
        raise CustomJsonException(code=codes.DOES_NOT_EXIST)
