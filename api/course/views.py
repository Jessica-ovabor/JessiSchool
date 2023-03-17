from flask import jsonify
from flask_restx import Namespace,Resource,fields
from ..utils import db
from ..utils.decorators import admin_required, get_user_type
from ..models.courses import Course,StudentCourse
from ..models.users import Student
from http import HTTPStatus
from flask_jwt_extended import jwt_required,get_jwt_identity,get_jwt

course_namespace=Namespace("course" , description="name space for authentication")
course_create_model = course_namespace.model  (
    'CourseCreation',{
         
        'course_name':fields.String(required=True, description= "Course name"),
        'course_code' :fields.String(required=True, description= "Course code"),
        'teacher' :fields.String(required=True, description= "Course teacher") ,
           
  
    }
)  
course_model = course_namespace.model(
    'AllCourses', {
        'course_name':fields.String( description= "Course name"),
        'course_code' :fields.String( description= "Course code"),
        'teacher' :fields.String(description= "Course teacher") ,
        'course_unit' :fields.String(description= "Course unit") ,
    }
)   
student_course_model = course_namespace.model(
    'StudentCourse', {
        'student_id': fields.Integer(description="Student's User ID"),
        'course_id': fields.Integer(description="Course's ID")
    }
)
def is_student_or_admin(student_id:int) -> bool:
    claims = get_jwt()
    active_user_id = get_jwt_identity()
    if (get_user_type(claims['sub']) == 'admin') or (active_user_id == student_id):
        return True
    else:
        return False      

@course_namespace.route('/register')
class AdminRegisterCourse(Resource):
    @course_namespace.expect(course_create_model)
    @course_namespace.doc(
        description='Register a Course - Admins Only'
    )
    @admin_required()
    def post(self):
        """
            Register a Course - Admins Only
        """
        data = course_namespace.payload

        #Check if course already exists
        course = Course.query.filter_by(course_name=data['course_name']).first()
        if course:
          return {"message": "Course Already Exists"}, HTTPStatus.CONFLICT

        # Register new course
        new_course = Course(
        course_name = data['course_name'],
        teacher = data['teacher'],
        course_unit="3",
        course_code=data['course_code'],
        
        
        )

        new_course.save()

        course_resp = {}
        course_resp['id'] = new_course.id
        course_resp['course_name'] = new_course.course_name
        course_resp['teacher'] = new_course.teacher
        course_resp['course_unit'] = new_course.course_unit
        course_resp['course_code'] = new_course.course_code

        return course_resp, HTTPStatus.CREATED
  
@course_namespace.route('')
class GetAllCourses(Resource):
    @course_namespace.marshal_list_with(course_model)
    @course_namespace.doc(
        description = "Get All Courses in the School_only signed in user be it an admin or student or visitor"
    )
    @jwt_required()
    def get(self):
        """
            Get All Courses in the school
        """
        courses = Course.query.all()

        return courses ,HTTPStatus.OK
    
   
@course_namespace.route('/<int:student_id>/courses')
class GetStudentCourses(Resource):

    @course_namespace.doc(
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
                course_resp['course_code'] = course.course_code
                course_resp['course_unit'] = course.course_unit

                resp.append(course_resp)

            return resp, HTTPStatus.OK
    
        else:
            return {"message": "Admins or Specific Student Only"}, HTTPStatus.FORBIDDEN


@course_namespace.route('/<int:course_id>/students/<int:student_id>')
class AddDropCourseStudent(Resource):
    
    @course_namespace.doc(
        description = "Enroll a Student for a Course by Admins Only",
        params = {
            'course_id': "The Course's ID"
        }
    )
    @admin_required()
    def post(self, course_id, student_id):
        """
            Enroll a Student for a Course by Admins Only
        """
        course = Course.get_by_id(course_id)
        student = Student.get_by_id(student_id)
        
        student_in_course = StudentCourse.query.filter_by(
                student_id=student.id, course_id=course.id
            ).first()
        if student_in_course:
            return {
                "message": f"Hello {student.name} with email of  {student.email} is already registered for {course.course_name}"
            }, HTTPStatus.OK
        
        course_student =  StudentCourse(
            course_id = course_id,
            student_id = student_id
        )

        course_student.save()

        course_student_resp = {}
        course_student_resp['course_id'] = course_student.course_id
        course_student_resp['course_name'] = course.course_name
        course_student_resp['teacher'] = course.teacher
        course_student_resp['student_id'] = course_student.student_id
        course_student_resp['student_name'] = student.name
        course_student_resp['student_email'] = student.email
        course_student_resp['matric_no'] = student.matric_no

        return course_student_resp, HTTPStatus.CREATED

    @course_namespace.doc(
        description='Remove a Student from a Course',
        params = {
            'course_id': "The Course's ID",
            'student_id': "The Student's ID"
        }
    )
    @admin_required()
    def delete(self, course_id, student_id):
        """
            Remove a Student from a Course - Admins Only
        """

        # Confirm existence of student and course
        course = Course.query.filter_by(id=course_id).first()
        student = Student.query.filter_by(id=student_id).first()
        if not student or not course:
            return {"message": "Student is not registered for this course "}, HTTPStatus.NOT_FOUND
        
        # Check if student is not registered for the course
        student_in_course = StudentCourse.query.filter_by(
                student_id=student.id, course_id=course.id
            ).first()
        if not student_in_course:
            return {
                "message": f"{student.name} with username of {student.username} is not registered for {course.course_name}"
            }, HTTPStatus.NOT_FOUND

        # Remove the student from the course
        student_in_course.delete()

        return {"message": f"{student.name} of matric_no: {student.matric_no} has been successfully removed from {course.course_name}"}, HTTPStatus.OK
@course_namespace.route('/<int:course_id>/enrolled')
class ListCourseEnrollment(Resource):
    @course_namespace.doc(
        description = "List the number of student enrollment in a particular Course - Admins",
        params = {
            'course_id': "The course ID"
        }
    )
    @admin_required()
    def get(self,course_id,):
        
        
        course = StudentCourse.query.get(course_id)
        
        if not course:
            return {'error': 'Course not found.'}, HTTPStatus.NOT_FOUND
        Total_student_enrolled = len(str(course.course_id))

        return jsonify({'Total student enrolled for this course is': Total_student_enrolled})
    