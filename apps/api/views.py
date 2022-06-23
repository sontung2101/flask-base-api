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
from helpers.middlewares import has_permission


class StudentsList(Resource):
    def get(self):
        students = Students.objects().all()
        schema = StudentsSchema(many=True)
        result = schema.dump(students)
        if students:
            return result
        raise CustomJsonException(code=codes.EMPTY_DATA)

    def post(self):
        try:
            count = 0
            while count < 3:
                # mock data
                random_id = str(uuid.uuid1())
                bttf = Students(student_no=random_id[:8], name=f"user_{random_id[:8]}",
                                img_url=f"image_url_{random_id[:8]}", email=f"email_{random_id[:8]}@gmail.com")
                bttf.save()
                count += 1
            return {"created": f" {count} students"}
        except Exception as exc:
            raise CustomJsonException(message=exc, status_code=402)


class StudentView(Resource):

    @has_permission('admin')
    def get(self, id):
        try:
            student = Students.objects.get(id=id)
        except Exception as exc:
            raise CustomJsonException(message=exc)
        schema = StudentsSchema()
        result = schema.dump(student)
        return result

    @has_permission('admin')
    def post(self, id):
        json_data = request.get_json()
        if not json_data:
            raise CustomJsonException(code=codes.NO_INPUT_DATA)
        quote_schema = StudentsSchema()

        try:
            data = quote_schema.load(json_data)
        except ValidationError as err:
            raise CustomJsonException(message=err.messages, code=422)

        try:
            student = Students.objects(id=id).first()
            if student is None:
                raise CustomJsonException(code=codes.DOES_NOT_EXIST)

            # update a student
            student.name = data.get("name", student.name)
            student.student_no = data.get("student_no", student.student_no)
            student.img_url = data.get("img_url", student.img_url)
            student.email = data.get("email", student.email)

            student.save()
            result = quote_schema.dump(student)
            return result
        except Exception as exc:
            raise CustomJsonException(message=exc)

    def delete(self, id):
        student = Students.objects(id=id).first()
        if student is not None:
            student.delete()
            return {"message": f"successfully deleted {id}"}
        raise CustomJsonException(code=codes.DOES_NOT_EXIST)


class CreateStudentView(Resource):
    def post(self):
        json_data = request.get_json()
        if not json_data:
            raise CustomJsonException(code=codes.NO_INPUT_DATA)
        quote_schema = StudentsSchema()

        try:
            data = quote_schema.load(json_data)

        except ValidationError as err:
            raise CustomJsonException(message=err.messages, code=422)

        try:
            student = Students(student_no=data["student_no"], name=data["name"],
                               img_url=data["img_url"], email=data["email"])
            student.save()
            result = quote_schema.dump(student)
            return {"message": "successfully updated ", "payload": result}
        except Exception as exc:
            raise CustomJsonException(message=exc)


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
