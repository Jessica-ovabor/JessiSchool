from flask_jwt_extended import get_jwt , verify_jwt_in_request
from functools import wraps
from flask import jsonify
from http import HTTPStatus
from ..models.users import User



def get_user_type(id:int):
    user = User.query.filter_by(id=id).first()
    if user:
        return user.user_type
    else:
        return None

# Custom decorator to verify admin access
def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if get_user_type(claims['sub']) == 'admin':
                return fn(*args, **kwargs)
            else:
                return {"message": "Administrator access required"}, HTTPStatus.FORBIDDEN
        return decorator
    return wrapper


def student_required():
    """
    A decorator to protect an endpoint with JSON Web Tokens.
    Any route decorated with this will require a user type of student  to be present in the
    request before the endpoint can be called.
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args,**kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if get_user_type(claims['sub']) == 'student' :
                return fn(*args,**kwargs)
            return jsonify({'msg': "Student Only!" }) , HTTPStatus.UNAUTHORIZED
        return decorator
    return wrapper


