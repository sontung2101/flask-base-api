import base64
import os

from flask_restful import reqparse, abort, Resource
from apps.api.models import Students
from helpers import codes
from helpers.exception import CustomJsonException
import uuid
from .schemas import StudentsSchema
from flask import request, current_app
from marshmallow import ValidationError
from werkzeug.utils import secure_filename

# from main import app
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


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


class UploadFileView(Resource):
    @staticmethod
    def read_base64(file):
        return base64.b64encode(file.read()).decode("utf-8")

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        files = request.files
        allowed = request.args.get('allowed', 'images', str)

        media = files['media']

        # check if the post request has the file part
        if 'media' not in files:
            raise CustomJsonException(code=codes.EXTENSIONS_NOT_ALLOWED)

        if media.filename == '':
            raise CustomJsonException(code=codes.EXTENSIONS_NOT_ALLOWED)

        if media and self.allowed_file(media.filename):
            filename = secure_filename(media.filename)
            media.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            media_base64 = self.read_base64(media)
            if allowed == 'images':
                media_base64 = f'data:image/jpeg;base64,{media_base64}'

            return {"message": "File successfully uploaded", "url": media_base64}

        raise CustomJsonException(code=codes.EXTENSIONS_NOT_ALLOWED)
