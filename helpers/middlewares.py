from functools import wraps


def has_permission(permission_name):
    print("Inside has_permission()")

    def decorator(f):
        print("Inside decorator()")

        @wraps(f)
        def decorated_function(*args, **kwargs):
            print("Inside decorated_function()")
            print(permission_name)
            # check permission
            # todo
            return f(*args, **kwargs)

        return decorated_function

    return decorator
