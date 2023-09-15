from flask import request,session
from flask_restx import Namespace,Resource,fields
from ..utils import db
from ..utils.decorators import admin_required,student_required,get_user_type
from ..utils import matric_no
from ..utils.grades import get_letter_grade,convert_grade_to_gpa
from ..models.courses import Course,StudentCourse,Score
from ..models.users import User,Admin,Student
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity,unset_jwt_cookies,get_jwt

student_namespace=Namespace("student" , description="name space for authentication")
student_signup_model = student_namespace.model(
    'StudentSignup',{
        
        "name":fields.String(required=True, description= "A name"),
        "username": fields.String(required=True, description= "A username"),
        "password": fields.String(required=True, description= "A password for student"),
        "email": fields.String(required=True, description= "An email for student"),
        
  
    }
)
student_model = student_namespace.model(
    'Student',{
        "id": fields.Integer(),
        "name":fields.String(description= "A name"),
        "username": fields.String( description= "A username"),
        "email": fields.String( description= "An email"),
        'user_type': fields.String(required=True, description="Type of User"),
        'matric_no': fields.String(required=True, description="Student matric_no"),
        "password_hash": fields.String(description= "A password"),
       
       
       
    }        
) 
student_course_model = student_namespace.model(
    'StudentCourse', {
        'student_id': fields.Integer(description="Student's User ID"),
        'course_id': fields.Integer(description="Course's ID")
    }
)

grade_model = student_namespace.model(
    'Grade', {
        'id': fields.Integer(description="Grade ID"),
        'course_id': fields.Integer(required=True, description="Course ID"),
        'score': fields.Float(required=True, description="Grade in Numbers Only")       
    }
)

grade_update_model = student_namespace.model(
    'GradeUpdate', {
        'grade': fields.String(required=True, description="Grade in Letter Only")       
    }
)

# Verify student or admin access
def is_student_or_admin(student_id:int) -> bool:
    claims = get_jwt()
    active_user_id = get_jwt_identity()
    if (get_user_type(claims['sub']) == 'admin') or (active_user_id == student_id):
        return True
    else:
        return False
#A global function to autogenerate password for student
  

@student_namespace.route('/register')
class StudentSignup(Resource):
    @student_namespace.expect(student_signup_model)
    @student_namespace.marshal_with(student_model)#marshal_with return json rather than object in db we use it to serialise
    @student_namespace.doc(
        description="Sign up a student by admin"
    )
    @admin_required()
    def post(self):
        """
        Sign up a student by an admin
        
        """
        data = request.get_json()
        student = Student.query.filter_by(email=data.get('email')).first()
        if student:
            return {'message':'Student already exists'},HTTPStatus.CONFLICT
       

        new_student = Student(
                email = data.get('email'),
                name = data.get('name'),
                username=data.get('username'),
                user_type = "student",
                password_hash = generate_password_hash(data.get('password')),
                
            )
        new_student.save()
        new_student.matric_no=matric_no(new_student.id)
        db.session.commit()
      
      
        return new_student, HTTPStatus.CREATED
#login model serialiser       
login_model = student_namespace.model(
    'Login',{
       
        "email": fields.String(required=True, description= "email"),
        "password": fields.String(required=True, description= "A password")
  
        
        
    }
) 
 
@student_namespace.route('/login')
@student_namespace.expect(login_model)
class Login(Resource):
    def post(self):
        """
        Login an admin  and Generate token
        
        """
        
        
        data= request.get_json()
        email=data.get('email')
        password=data.get('password')
        
        #checks if in the database if for instance ovaj@gmail.com exixts in our dable it grabs the whole info about that note emailmis set to be unique
        user = Student.query.filter_by(email=email).first()
     
        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity= user.id)
            refresh_token = create_refresh_token(identity= user.id)  
            
            
            response ={
                
                'access_token':access_token,
                'refresh_token':refresh_token,
                'message':'You have successfully logged-in',
                
            }
        else:
            response={
                'message':'Oops incorrect username or password'
            }
            return response,HTTPStatus.BAD_REQUEST
        return response, HTTPStatus.CREATED
@student_namespace.route('/logout')
class Logout(Resource):
    @student_required()
    def post(self):
        """
        Logout a User
       
        """
        unset_jwt_cookies
        db.session.commit()
        return {"message":"Student logged out successfully"},HTTPStatus.OK
#it refreshes and return a username  and our authentication endpoint     
@student_namespace.route('/refresh')
class Refresh(Resource):    
    @jwt_required(refresh=True)
    def post(self):
        """
        refresh token
       
        """
        username =get_jwt_identity()
        
        access_token = create_access_token(identity=username)
        
        return{"access_token":access_token }, HTTPStatus.OK
#Get All Student
@student_namespace.route('')
class GetAllStudent(Resource):
    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="Retrieve all student by admin"
    )

    @admin_required()
    def get(self):
        """
        Retrieve all registered student by admin
        """
        student =Student.query.all()
        return student,HTTPStatus.OK

@student_namespace.route('/<int:student_id>')
class AdminRetrieveStudent(Resource):

    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="""
            This endpoint is accessible only to an admin and teacher. 
            It allows the  retrieval of a student
            """
    )
    @admin_required()
    def get(self, student_id):
        """
        Retrieve a student 
        """
        student = Student.query.filter_by(id=student_id).first()
        if not student:
            return {'message':'Student does not exist'}, HTTPStatus.NOT_FOUND
        return student , HTTPStatus.OK
@student_namespace.route('/<int:student_id>')
class GetUpdateDeleteStudents(Resource):
    
    @student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="Retrieve a student's details by ID",
        params = {
            'student_id': "The Student's ID"
        }
    )
    @student_required()
    def get(self, student_id):
        """
            Retrieve a Student's Details by ID
        """
        student = Student.get_by_id(student_id)
        
        return student,HTTPStatus.OK
   
   
      
    
    @student_namespace.expect(student_signup_model)
    #@student_namespace.marshal_with(student_model)
    @student_namespace.doc(
        description="Update a student's details by ID",
        params = {
            'student_id': "The Student's ID"
        }
    )
    @student_required()
    def put(self, student_id):
        """
            Update a Student's Details by ID
        """ 
        student = Student.get_by_id(student_id)
        active_student =get_jwt_identity()
        if active_student != student:
            return {'message': 'Only student with this account  can update the details'}
        
        data = student_namespace.payload
        

        # student.name = data['name']
        # student.username = data['username']
        # student.email = data['email']
        student.password_hash = generate_password_hash(data['password'])

        db.session.commit()

        student_resp = {}  
        student_resp['id'] = student.id
        student_resp['name'] = student.name
        student_resp['username'] = student.username
        student_resp['email'] = student.email
        student_resp['user_type'] = student.user_type
        student_resp['matric_no'] = student.matric_no
        student_resp['password_hash'] = student.password_hash
        


        return student_resp,HTTPStatus.OK
    
    @student_namespace.doc(
        description='Delete a student by ID',
        params = {
            'student_id': "The Student's ID"
        }
    )
    @admin_required()
    def delete(self, student_id):
        """
            Delete a student by ID - Admins Only
        """
        students= Student.get_by_id(student_id)
        
        students.delete()

        return {"message": "Student Successfully Deleted"}, HTTPStatus.OK   
#Score and grade for student


@student_namespace.route('/<int:student_id>/courses')
class GetStudentCourses(Resource):

    @student_namespace.doc(
        description = "Retrieve a Student's Courses - Admins or Specific Student Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    @jwt_required()
    def get(self, student_id):
        """
            Retrieve a Student's Courses - Admins or Specific Student Only
        """
        if is_student_or_admin(student_id):
            
            courses = StudentCourse.get_courses_by_student(student_id)
            resp = []

            for course in courses:
                course_resp = {}
                course_resp['id'] = course.id
                course_resp['course_name'] = course.course_name
                course_resp['teacher'] = course.teacher
                course_resp['course_unit'] = course.course_unit

                resp.append(course_resp)

            return resp, HTTPStatus.OK
    
        else:
   
            return {"message": "Admins or Authorised Student Only"}, HTTPStatus.FORBIDDEN


@student_namespace.route('/<int:student_id>/grades')
class GetAddUpdateGrades(Resource):

    @student_namespace.doc(
        description = "Retrieve a Student's Grades - Admins or Authorised Student Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    @jwt_required()
    def get(self, student_id):
        """
            Retrieve a Student's Grades - Admins or Specific Student Only
        """
        if is_student_or_admin(student_id):

            # Confirm existence of student
            student = Student.query.filter_by(id=student_id).first()
            if not student:
                return {"message": "Student Not Found"}, HTTPStatus.NOT_FOUND
            
            # Retrieve the student's grades        
            courses = StudentCourse.get_courses_by_student(student_id)
            resp = []

            for course in courses:
                grade_resp = {}
                grade_in_course = Score.query.filter_by(
                        student_id=student_id, course_id=course.id
                    ).first()
                grade_resp['course_name'] = course.course_name

                if grade_in_course:
                    grade_resp['grade_id'] = grade_in_course.id
                    grade_resp['score'] = grade_in_course.score
                    grade_resp['grade'] = grade_in_course.grade
                else:
                    grade_resp['score'] = None
                    grade_resp['grade'] = None
                
                resp.append(grade_resp)
            
            return resp, HTTPStatus.OK
        
        else:
            return {"message": "Admins or Authorised Student Only"}, HTTPStatus.FORBIDDEN
        
    @student_namespace.expect(grade_model)
    @student_namespace.doc(
        description = "Upload a Student's Grade in a Course by Admins Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    @admin_required()
    def post(self, student_id):
        """
            Upload a Student's Grade in a Course - Admins Only
        """
        data = student_namespace.payload

        student = Student.get_by_id(student_id)
        course = Course.get_by_id(id=data['course_id'])
        
        # Confirm that the student is taking the course
        student_course = StudentCourse.query.filter_by(student_id=student_id, course_id=course.id).first()
        if not student_course:
            return {"message": f" hello {student.name}of username {student.username} is not taking {course.course_name}"}, HTTPStatus.NOT_FOUND
        
        # Add a new grade
        new_grade = Score(
            student_id = student_id,
            course_id = data['course_id'],
            score = data['score'],
            grade = get_letter_grade(data['score'])
        )

        new_grade.save()

        grade_resp = {}
        grade_resp['course_id'] = new_grade.course_id
        grade_resp['course_name'] = course.course_name
        grade_resp['course_teacher'] = course.teacher
        grade_resp['grade_id'] = new_grade.id
        grade_resp['student_id'] = new_grade.student_id
        grade_resp['student_name'] = student.name
        grade_resp['student_username'] = student.username
        grade_resp['student_matric_no'] = student.matric_no
        grade_resp['student_course _unit'] = course.course_unit
        grade_resp['score'] = new_grade.score
        grade_resp['grade'] = new_grade.grade

        return grade_resp, HTTPStatus.CREATED
        

@student_namespace.route('/grades/<int:grade_id>')
class UpdateDeleteGrade(Resource):

    @student_namespace.expect(grade_update_model)
    @student_namespace.doc(
        description = "Update a Grade - Admins Only",
        params = {
            'grade_id': "The Grade's ID"
        }
    )
    @admin_required()
    def put(self, grade_id):
        """
            Update a Grade - Admins Only
        """
        data = student_namespace.payload

        grade = Score.get_by_id(grade_id)
        
        grade.score = data['grade']
        grade.letter_grade = get_letter_grade(data['grade'])
        
        db.session.commit()

        grade_resp = {}
        grade_resp['grade_id'] = grade.id
        grade_resp['student_id'] = grade.student_id
        grade_resp['course_id'] = grade.course_id
        grade_resp['score'] = grade.score
        grade_resp['grade'] = grade.letter_grade

        return grade_resp, HTTPStatus.OK
    
    @student_namespace.doc(
        description = "Delete a Grade - Admins Only",
        params = {
            'grade_id': "The Grade's ID"
        }
    )
    @admin_required()
    def delete(self, grade_id):
        """
            Delete a Grade - Admins Only
        """
        grade = Score.get_by_id(grade_id)
        
        grade.delete()

        return {"message": "Grade Successfully Deleted"}, HTTPStatus.OK
        
    
@student_namespace.route('/<int:student_id>/cgpa')
class GetStudentCGPA(Resource):

    @student_namespace.doc(
        description = "Calculate a Student's CGPA - Admins or Specific Student Only",
        params = {
            'student_id': "The Student's ID"
        }
    )
    @jwt_required()
    def get(self, student_id):
        """
            Calculate a Student's CGPA - Admins or Specific Student Only
        """
 
                    
   
        if is_student_or_admin(student_id):

            student = Student.get_by_id(student_id)
            
            courses = StudentCourse.get_courses_by_student(student_id)
            
            total_grade_points = 0
            
            total_gpa=0

        for course in courses:
            grade = Score.query.filter_by(
                        student_id=student_id, course_id=course.id
                    ).first()
            if grade:
                letter_grade = grade.grade
                gpa = convert_grade_to_gpa(letter_grade)
                total_gpa = gpa+total_gpa 
                
                grade_points = grade.score * course.course_unit
                total_grade_points  = grade_points+course.course_unit
            
            cgpa = total_grade_points / grade_points
            
            round_cgpa = float("{:.2f}".format(cgpa))
            
            
            
  
            return {"message": f"Hello {student.name} your total CGPA is {round_cgpa} and according to our school standard {convert_grade_to_gpa(round_cgpa)}"}, HTTPStatus.OK
    
        else:
            return {"message": "Admins or Specific Student Only"}, HTTPStatus.FORBIDDEN