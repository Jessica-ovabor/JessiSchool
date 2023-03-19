# JessiSchool
Contributors Forks Stargazers Issues MIT License Twitter

Student Management API
Explore the Documentation »
View Demo · Report Bug · Request Feature

Table of Contents
About Student Management API
Student Management API does the main function of a school and explains how it works. It enables the school to create an admin account. It allows the registration of students and lecturers. Also, the API allows the school admin to create courses and handling the grading system for the student.

CRUD operations can be carried out on the student data and the courses data, with an easy-to-use Swagger UI setup for testing and integration with the front end.

A Student account have limited access to the app, as a student can only change their profile details and view their profile, courses, grades and GPA.

This Student Management API was built with Python's Flask-RESTX by Ajayi Oluwaseyi during Backend Engineering live classes at AltSchool Africa. This was built as my third semester final capstone project in AltSchool Africa.

back to top

Built With:
Python Flask SQLite

back to top

Knowledge Acquired
Creating this API helped me learn and practice:

API Development with Python
Unit Testing using pytest and Postman
Routing
Swagger Documentation
Debugging
Database Management
App Security
User Authentication and Authorization
back to top

Project Scope
The Student Management API handles the following:

Admin Registration
Lecturer Registration
Student Registration
Getting Student Information and applying the CRUD operation
Course Creation
Getting a Course details and using the CRUD operation
Multiple Course Registration for Students
Assigning a Lecturer to a course
Adding a Student Score
Calculating a Student GPA using the 4.0 Grading System.
The future Versions will cover more aspects and features as needed soon.

Usage
To explore and use this API, follow these steps:

Open the web app on your browser: https://student-flask-api.herokuapp.com/

Create an admin or student or lecturer account:

Click 'auth' to reveal a dropdown menu of the authentication routes, then register an admin account via the '/auth/signup' route. Input your details and input 'admin' in the 'user-type' to create an admin account.
Click 'auth' to reveal a dropdown menu of the authentication routes, then register a student account via the '/auth/signup' route. Input your details and input 'student' in the 'user-type' to create an admin account.
Click 'auth' to reveal a dropdown menu of the authentication routes, then register a lecturer account via the '/auth/signup/lecturer' route. Input your details to create a lecturer account.
Login via the '/auth/login' route to generate a JWT token. Copy the access token only without the quotation marks

Scroll back up to click Authorize at top right. Enter the JWT token in the given format, for example:

Bearer eyJhbtestXVCJ9.eyJbmMzd9.this_rQh8_tl2V1iDlsl_wAOMHcing5334
Click Authorize and then Close.

Now authorized, you can create, view, update and delete students, courses and grades via the routes in 'students' and 'courses'. You can also see the information about:

All students taking a course
All courses taken by a student
A student's grades in percentage (example: 84.0) and letters (eg: B+)
A student's GPA, calculated using the 4.0 grading system based on all grades from all courses they are taking (example: 3.3)
Go to the Course Namespace and create a new course before adding a student to the course

Then go on ahead to perform other operations and test all the routes. Enjoy!

When you're done, click 'Authorize' at top right again to then 'Logout'. Also, head on to the '/auth/logout' route to log the user out and revoke the access token.

Note: Any registered user can request to reset their password through the '/auth/password-reset-request' route and the link to reset their password will be sent to the user's mail. Copy the token from the link that was sent to your mail and paste it in the token field in the '/auth/password-reset/' route. Then you can go on to change your password.

back to top

Installation
Clone the repository to your local machine.
Navigate to the project directory.
Create a virtual environment and activate it:
Open the requirements.txt file amd remove the uwsgi package
Install the dependencies:
Run the application:
To create a virtual environment called 'venv' and activate it.
python -m venv venv
source venv/bin/activate
Note: Open the requirements.txt file and remove the uwsgi package which is also the last package. It is likely for you to run into an error if you don't remove it because this is the dyno used to run the app on heroku and will not work on your local machine. After doing this, you can go ahead and install the rest with this command.

pip install -r requirements.txt
To create your database locally.
flask shell     # press enter
db              # press enter
User            # press enter
Admin           # press enter
Student         # press enter
Course          # press enter
StudentCourse   # press enter
Score           # press enter
db.create_all() # press enter
exit()          # press enter
Finally, To run the application.
python app.py
Endpoints for the Student Management API
Auth EndPoint
ROUTE	METHOD	DESCRIPTION	AUTHORIZATION	USER TYPE
/auth/signup	POST	Creation of students and admin account	None	Any
/auth/login	POST	Creation of JWT Tokens for students and admin	None	Any
/auth/refresh	POST	Creation of Access Tokens for all account	Bearer Refresh-Token	Any
/auth/signup/lecturer	GET	Creation of lecturers account	Bearer Access-Token	Admin
/auth/logout	POST	LogOut User and revoke access/refresh tokens	Bearer Access-Token	Any
/auth/password-reset-request	POST	Request for password reset	None	Any
/auth/password-reset/{token}	POST	Reset password	None	Any
Student EndPoint
ROUTE	METHOD	DESCRIPTION	AUTHORIZATION	USER TYPE
/students/	GET	Get all Students	Bearer Access-Token	Admin
/students/studentcourse/score/{course_id}	PUT	Update a student course score by the course lecturer	Bearer Access-Token	Lecturer
/students/{student_id}	GET	Get a student by ID	Bearer Access-Token	Admin or Lecturer
/students/{student_id}	DELETE	Delete a student by ID	Bearer Access-Token	Admin
/students/{student_id}	PUT	Update a student by ID	Bearer Access-Token	Admin or Lecturer
/students/{student_id}/courses	GET	Get a student courses by ID	Bearer Access-Token	Admin or Lecturer
/students/{student_id}/courses/grades	GET	Get a student all courses and grades by ID	Bearer Access-Token	Admin or Lecturer
/students/{student_id}/{course_id}/gpa	GET	Calculate a Student Course GPA	Bearer Access-Token	Admin or Lecturer
Course EndPoint
ROUTE	METHOD	DESCRIPTION	AUTHORIZATION	USER TYPE
/courses/	GET	List all courses available	Bearer Access-Token	Any
/courses/	POST	Create a new course	Bearer Access-Token	Admin
/courses/addcourse/{course_id}	DELETE	Delete a student from a course	Bearer Access-Token	Lecturer
/courses/addcourse/{course_id}	POST	Register a student to a course	Bearer Access-Token	Lecturer
/courses/{course_id}	GET	Get a course by ID	Bearer Access-Token	Any
/courses/{course_id}	DELETE	Delete a course by ID	Bearer Access-Token	Admin
/courses/{course_id}/students	GET	List all registered students in a course	Bearer Access-Token	Admin or lecturer
Sample

Student Management API Screenshot


back to top

License
Distributed under the MIT License. See LICENSE for more information.

back to top

Contact
You can contact me with my social media handles:

LinkedIn | Twitter | Github | Email: oluwaseyitemitope456@gmail.com

Project Link: Student Management API

back to top

Acknowledgements
This project was made possible by:

AltSchool Africa School of Engineering
Caleb Emelike
