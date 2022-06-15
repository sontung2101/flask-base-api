from apps.api import views


def views_routes(api, prefix):
    api.add_resource(views.Student, f'{prefix}/students/<pk>')
    api.add_resource(views.StudentsList, f'{prefix}/students')