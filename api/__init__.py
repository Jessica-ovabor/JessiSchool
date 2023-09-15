from flask import Flask
from flask_restx import Api
from .course.views import course_namespace
from .auth.views import auth_namespace
from .students.views import student_namespace
from .config.config import config_dict
from .utils  import db
from .models.users import User,Admin,Student
from .models.courses import Course,StudentCourse,Score
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound,MethodNotAllowed



def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    #configure the dev so we can use it
    app.config.from_object(config)
    db.init_app(app)
    jwt = JWTManager(app)
    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': "Authorization",
            "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; ** token to authorize"
        }
    }

    api = Api(
        app, 
        version='1.0', 
        title='Student Management API', 
        description='A simple Student Management REST API service',
        authorizations=authorizations,
        security='apikey'
    )

    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(student_namespace, path='/student')
    api.add_namespace(course_namespace, path='/course')

    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Not Found"}, 404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error": "Method Not Allowed"}, 404

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Admin': Admin,
            'Score': Score,
            'Course': Course,
            'Student': Student,
            'StudentCourse': StudentCourse
        }

        


    
    return app