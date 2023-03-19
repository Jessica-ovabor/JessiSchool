<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<!-- Project Name -->
<div align="center">
  <h1>JessiSchool</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/Jessica-ovabor
/JessiSchool#readme"><strong>Explore the Documentation »</strong></a>
    <br />
    <a href="https://github.com/Jessica-ovabor
/JessiSchool/blob/main/images/student_api_full_page.png">View Demo</a>
    ·
    <a href="https://github.com//Jessica-ovabor
/JessiSchool/issues">Report Bug</a>
    ·
    <a href="https://github.com/Jessica-ovabor
/JessiSchool/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-student-api">About Student Management API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#knowledge-acquired">Knowledge Acquired</a></li>
    <li><a href="#project-scope">Project Scope</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#installaton">Installation</a></li>
    <li><a href="#sample">Sample</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Project -->
## About Student Management API

Student Management API does the main function of a university system and explains how it works. It enables the school to create an admin account. It allows the registration of students by admin. Also, the API allows the school admin to create courses and handling the grading system for the student and student cgpa on a scale of 4.0.

CRUD operations can be carried out on the admin data ,student data and the courses data, with an easy-to-use Swagger UI setup for testing and integration with the front end.

A Student account have restricted access to the app, as a student can only change their profile details and view their profile, courses, grades and CGPA.

This Student Management API was built with Python's Flask-RESTX a python Api by <a href="https://www.github.com/Jessica-ovabor">Jessica Ovabor</a> during Backend Engineering live classes at <a href="https://altschoolafrica.com/schools/engineering">AltSchool Africa</a>. This was built as my third semester final capstone project in <b>AltSchool Africa</b>. 

<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## Knowledge Acquired

Creating this API helped me learn and practice:
* API Development with Python
* Unit Testing using pytest and Postman
* Routing
* Swagger Documentation
* Debugging
* Database Management
* App Security
* User Authentication and Authorization
* Flask Admin Permissions and Restriction
* Deployment

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- What the API can do -->
## Project Scope

The Student Management API handles the following:
* Admin Registration
* Admin Authentication and Authorisations
* Admin CRUD operation
* Student Registration-Admins
* Student Authentication and Authorisations
* Getting Student Information and applying the CRUD operation
* Course Creation-course units
* Getting a Course details and using the CRUD operation
* Multiple Course Registration for Students
* Assigning a Teacher to a course
* Get all Availaible Course in the School-Any signed in user
* List the Total enrollment to a Course
* Removing a Student from a Course
* Adding a Student Score and Letter Grade
* Calculating a Student CGPA using the 4.0 Grading System.
* Retrieve all registered student or admin in the school
* Specifying Usertype -'admin' or'student'
* Assigning a unique matric_no to student which is a combination of the school name,the course(PYT), and id as of when the student registered n the portal of the format-ALT/PYT/0001

The future Versions will cover payment ,statement of result and features as needed soon.

---

<!-- GETTING STARTED -->
## Usage

To explore and use this API, follow these steps:

1. Open the web app on your browser: https://jovabor.pythonanywhere.com/

2. Create an admin account:
   - Click 'auth' to reveal a dropdown menu of the authentication routes, then register an admin account via the '/auth/register/admin' route. Input your details and a type 'admin' will be assigned. to create an admin account.
 Create a student account:
   - Click 'student' to reveal a dropdown menu of the authentication routes, then register an admin account via the '/student/register' route. Input your details and a type 'student' will be assigned.
  
3.  Login a Student or Admin account:
    -Login via the '/auth/login' route to generate a JWT token. Copy the access token only without the quotation marks- to login an admin
    -Login via the '/student/login' route to generate a JWT token. Copy the access token only without the quotation marks- to login a student

4. Scroll back up to click <b>Authorize</b> at top right. Enter the JWT token in the given format, for example:
   ```
   Bearer eyJhbtestXVCJ9.eyJbmMzd9.this_rQh8_tl2V1iDlsl_wAOMHcing5334
   ```

5. Click <b>Authorize</b> and then <b>Close</b>.

6. Now authorized, you can create, view, update and delete students, courses and grades via the routes in <b>'students'</b> and **'courses'**. You can also see the information about:
    - All students taking a course
    - All courses taken by a student
    - A student's grades in percentage (example: 84.0) and letters (eg: B+)
    - A student's GPA, calculated using the 4.0 grading system based on all grades from all courses they are taking (example: 3.3)
    - All courses available in the school
   
7. Go to the **Course** Namespace and create a new course before adding a student to the course

8. Then go on ahead to perform other operations and test all the routes. <b>_Enjoy!_</b>

9. When you're done, click 'Authorize' at top right again to then 'Logout'. Also, head on to the **'/auth/logout'** route to log the user out and revoke the access token.

**Note:** Any registered user can request to update their details via **'/student/student_id'** route- input your id when your account was created
  

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Installing this app on your machine locally -->
## Installation

<div></div>
<ul style="font-size:18px;">
    <li>Clone the repository to your local machine.</li>
    <li>Navigate to the project directory.</li>
    <li>Create a virtual environment and activate it:</li>
    <li>Open the requirements.txt file amd remove the uwsgi package</li>
    <li>Install the dependencies:</li>
    <li>Run the application:</li>
</ul>

### To create a virtual environment called 'env' and activate it.

```console
python -m venv env
env/Scripts/Activate
```

**Note:** Open the requirements.txt file and remove the uwsgi package which is also the last package. It is likely for you to run into an error if you don't remove it because this is the dyno used to run the app on pythonanywhere and will not work on your local machine. After doing this, you can go ahead and install the rest with this command. 

```console
pip install -r requirements.txt
```

### To create your database locally.

```console
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
```

### Finally, To run the application.

```console
python runserver.py
```

# Endpoints for the Student Management API

<div style="margin-top:8px; margin-bottom:10px; font-size:20px; font-weight:bold;">Auth EndPoint For Admin</div>
<!-- Tables for routing in each models -->

| ROUTE                          | METHOD | DESCRIPTION                                   | AUTHORIZATION          | USER TYPE |
|--------------------------------| ------ |-----------------------------------------------|------------------------|-----------|
| `/auth/register/admin`         | _POST_ |  Creation of admin account                    |     `None`             | Admin     |
| `/auth/login`                  | _POST_ | Creation of JWT Tokens for  admin             |     `None`             | Admin     |
| `/auth/refresh`                | _POST_ | Creation of Access Tokens for all account     | `Bearer Refresh-Token` | Admin     |
| `/auth/logout`                 | _POST_ | LogOut User and revoke access/refresh tokens  | `Bearer Access-Token`  | Admin     |
| `/auth/admin`                  | _GET_  |  Get all registered user- admin and student   |  `Bearer Access-Token` | Admin     |
| `/auth/admin/admin_id`         | _DEL_  |  Delete an admin                              |   `Bearer Access-Token`| Admin     |



<div style="margin-top:20px; margin-bottom:10px; font-size:20px; font-weight:bold;">Student EndPoint</div>

| ROUTE                          | METHOD | DESCRIPTION                                   | AUTHORIZATION          | USER TYPE |
|--------------------------------| ------ |-----------------------------------------------|------------------------|-----------|
| `/student/register`            | _POST_ | Creation of student account by admin          |     `None`             | Admin     |
| `/student/login`               | _POST_ | Creation of JWT Tokens for  student           |     `None`             | Student   |
| `/student/refresh`             | _POST_ | Creation of Access Tokens for all account     | `Bearer Refresh-Token` | Student   |
| `/student/logout`              | _POST_ | LogOut User and revoke access/refresh tokens  | `Bearer Access-Token`  | Student   |
| `/student/student_id`          | _PUT_  | Update a student detail                       |  `Bearer Access-Token` | Student   |
| `/student/student_id`          | _GET_  | Get a student detail by admin or student      |  `Bearer Access-Token` |  Any      |
| `/student/student_id`          | _DEL_  | Delete a student detail by admin              |  `Bearer Access-Token` |  Admin    |
| `/student/grades/grades_id`    | _PUT_  | Update a student grade by admin               |  `Bearer Access-Token` |  Admin    |
| `/student/grades/grades_id`    | _DEL_  | Delete a student grade by admin               |  `Bearer Access-Token` |  Admin    |
| `/student/student_id/grades`   | _POST_ | Upload a student grade in a course            |  `Bearer Access-Token` |   Admin   |
| `/student/student_id/grades`   | _GET_  | Retrieve  a student grade in a course         |  `Bearer Access-Token` |   Any     |
| `/student/student_id/courses`  | _GET_  | Retrieve a student course                     |  `Bearer Access-Token` |   Any     |
| `/student/student_id/cgpa`     | _GET_  | Calculate a student cgpa                      |  `Bearer Access-Token` |   Any     |


<div style="margin-top:20px; margin-bottom:10px; font-size:20px; font-weight:bold;">Courses EndPoint</div>

| ROUTE                          | METHOD | DESCRIPTION                                   | AUTHORIZATION          | USER TYPE |
|--------------------------------| ------ |-----------------------------------------------|------------------------|-----------|
| `/course`                      | _GET_  | Get all courses in school                     |  `Bearer Access-Token` |   Any     |
| `/course/register`             | _POST_ | Register a student to a course                |  `Bearer Access-Token` |   Admin   |
| `/course/course_id/enrolled`   | _GET_  | Get the total number of enrollment to a course|  `Bearer Access-Token` |   Admin   |
| `/course/student_id/courses`   | _GET_  | Get tudent courses                            |  `Bearer Access-Token` |   Any     |



---

<!-- Sample Screenshot -->
## Sample

<br />

![JessiSchool](https://user-images.githubusercontent.com/74324460/226197363-ea88c83a-539e-4c28-baaa-f448c17fdc32.png)
![JessiSchool](https://user-images.githubusercontent.com/74324460/226197365-960c2d2a-fc65-4d97-b179-faf373e1c0e4.png)
 

<br/>

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/Jessica-ovabor/JessiSchoolblob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

You can contact me with my social media handles:

[LinkedIn](https://www.linkedin.com/in/jovabor) | [Twitter](https://twitter.com/jovabor) | [Github](https://github.com/Jessica-ovabor) | Email: ovaborjessica85@gmail.com

Project Link: [JessiSchool](https://github.com/Jessica-ovabor/JessiSchool)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike](https://github.com/CalebEmelike)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/Oluwatemmy/Student-Management-API.svg?style=for-the-badge
[contributors-url]: https://github.com/Oluwatemmy/Student-Management-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Oluwatemmy/Student-Management-API.svg?style=for-the-badge
[forks-url]: https://github.com/Oluwatemmy/Student-Management-API/network/members
[stars-shield]: https://img.shields.io/github/stars/Oluwatemmy/Student-Management-API.svg?style=for-the-badge
[stars-url]: https://github.com/Oluwatemmy/Student-Management-API/stargazers
[issues-shield]: https://img.shields.io/github/issues/Jessica-ovabor/JessiSchool.svg?style=for-the-badge
[issues-url]: https://github.com/Jessica-ovabor/JessiSchool/issues
[license-shield]: https://img.shields.io/github/license/Jessica-ovabor/JessiSchool.svg?style=for-the-badge
[license-url]: https://github.com/Jessica-ovabor/JessiSchool-API/blob/main/LICENSE
[twitter-shield]: https://img.shields.io/badge/-@jessica ovabor-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/ze_austin
[twitter-url]: https://twitter.com/jovabor
[JessiSchool-screenshot]: [Screenshot_20230319_063511]
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white!(https://user-images.githubusercontent.com/74324460/226195821-80565e9c-bc4a-450b-8f5f-aa2e4535ba83.png)
