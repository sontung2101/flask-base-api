from apps.api import views


def views_routes(api, prefix):
    api.add_resource(views.StudentView, f'{prefix}/students/<id>')
    api.add_resource(views.StudentsList, f'{prefix}/students')
    api.add_resource(views.UploadFileView, f'{prefix}/upload_file')
