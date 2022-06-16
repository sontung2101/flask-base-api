import base64
import os
import uuid

from flask_restful import Resource
from apps.api.models import Students
from helpers import codes, constants
from helpers.exception import CustomJsonException
from .schemas import StudentsSchema
from flask import request, current_app
from marshmallow import ValidationError
from werkzeug.utils import secure_filename


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
            # mock data
            random_id = str(uuid.uuid1())
            bttf = Students(student_id=random_id[:8], name=f"user_{random_id[:8]}",
                            img_url=f"image_url_{random_id[:8]}", email=f"email_{random_id[:8]}@gmail.com")
            bttf.save()
            return None
        except Exception as exc:
            raise CustomJsonException(message=exc, status_code=402)


class StudentView(Resource):

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
        if not json_data:
            raise CustomJsonException(code=codes.NO_INPUT_DATA)
        json_data["student_id"] = pk
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
            # update a student
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
            return {"message": f"successfully deleted {pk}"}
        raise CustomJsonException(code=codes.DOES_NOT_EXIST)


class UploadFileView(Resource):
    @staticmethod
    def read_base64(file):
        return base64.b64encode(file.read()).decode("utf-8")

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in constants.ALLOWED_EXTENSIONS

    def post(self):
        files = request.files
        base_64 = request.args.get('base64', "allowed", str)
        file = files['file']

        if 'file' not in files:
            raise CustomJsonException(code=codes.NO_FILE_PART)

        if file.filename == '':
            raise CustomJsonException(code=codes.NO_FILE_SELECTED)

        # return base64
        if base_64 == "allowed":
            file_base64 = self.read_base64(file)
            file_base64 = f'data:image/jpeg;base64,{file_base64}'
            return {"message": constants.SUCCESSFULLY_UPLOADED, "url": file_base64}

        # save file to static
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return {"message": constants.SUCCESSFULLY_UPLOADED}

        raise CustomJsonException(code=codes.EXTENSIONS_NOT_ALLOWED)
