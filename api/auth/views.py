from flask import request,session
from flask_restx import Namespace,Resource,fields
from ..utils import db
from ..utils.decorators import admin_required
from ..models.users import User,Admin
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity,unset_jwt_cookies,get_jwt


auth_namespace =Namespace("auth" , description="name space for authentication")
admin_signup_model = auth_namespace.model(
    'Signup',{
        
        "name":fields.String(required=True, description= "A name"),
        "username": fields.String(required=True, description= "A username"),
        "password": fields.String(required=True, description= "A password for admin"),
        "email": fields.String(required=True, description= "An email for admin"),
  
    }
)
admin_model = auth_namespace.model(
    'Admin',{
        "id": fields.Integer(),
        "name":fields.String(description= "A name"),
        "username": fields.String( description= "A username"),
        "email": fields.String( description= "An email"),
        'user_type': fields.String(required=True, description="Type of User"),
        "password_hash": fields.String(description= "A password"),
       
       
       
    }        
) 

@auth_namespace.route('/register/admin')
class Signup(Resource):
    
    @auth_namespace.expect(admin_signup_model)
    @auth_namespace.marshal_with(admin_model)#marshal_with return json rather than object in db we use it to serialise
    @auth_namespace.doc(
        description="Sign up an admin"
    )
    def post(self):
        """
        Sign up an admin
        
        """
         
        data = request.get_json()
        admin = Admin.query.filter_by(email=data.get('email')).first()
        if admin:
            return {'Message':'Admin already exists'},HTTPStatus.CONFLICT
       

        new_admin = Admin(
                email = data.get('email'),
                name = data.get('name'),
                username=data.get('username'),
                user_type = "admin",
                password_hash = generate_password_hash(data.get('password')),
                
            )
        new_admin.save()
      
      
        return new_admin,  HTTPStatus.CREATED       
#login model serialiser       
login_model = auth_namespace.model(
    'Login',{
       
        "email": fields.String(required=True, description= "email"),
        "password": fields.String(required=True, description= "A password")
  
        
        
    }
) 
 
@auth_namespace.route('/login')
@auth_namespace.expect(login_model)
class Login(Resource):
    def post(self):
        """
        Login an admin  and Generate token
        
        """
        
       
        data= request.get_json()
        email=data.get('email')
        password=data.get('password')
        
        #checks if in the database if for instance ovaj@gmail.com exixts in our dable it grabs the whole info about that note emailmis set to be unique
        user = User.query.filter_by(email=email).first()
     
        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity= user.id)
            refresh_token = create_refresh_token(identity= user.id)  
            
            
            response ={
                
                'access_token':access_token,
                'refresh_token':refresh_token,
                'message':'logged in successfully',
                
            }
        else:
            response={
                'message':'Oops incorrect password'
            }
            return response,HTTPStatus.BAD_REQUEST
        return response, HTTPStatus.CREATED
@auth_namespace.route('/logout')
class Logout(Resource):
    @jwt_required()
    def post(self):
        """
        Logout a User
       
        """
        unset_jwt_cookies
        db.session.commit()
        return {"message":"Logged out successfully"},HTTPStatus.OK
#it refreshes and return a username  and our authentication endpoint     
@auth_namespace.route('/refresh')
class Refresh(Resource):    
    @jwt_required(refresh=True)
    def post(self):
        """
        refresh token
       
        """
        username =get_jwt_identity()
        
        access_token = create_access_token(identity=username)
        
        return{"access_token":access_token }, HTTPStatus.OK
#Get All users
@auth_namespace.route('/admin')
class GetAllAdmin(Resource):
    @auth_namespace.marshal_with(admin_model)
    @auth_namespace.doc(
        description="Retrieve all users"
    )

    @admin_required()
    def get(self):
        """
        Retrieve all users registerd
        """
        users=User.query.all()
        return users,HTTPStatus.OK
#Delete admin by admin access
@auth_namespace.route('/admin/<int:admin_id>')
class DeleteAdmin(Resource):
 
    @auth_namespace.doc(
        description="delete an admin by ID",
        params={
            'admin_id':"The admin id"
            
        }
    )
    @admin_required()
    def delete(self,admin_id):
        """
        delete a admin by ID
        
        """
        
    
        admin =Admin.get_by_id(admin_id)
        admin.delete()
        return {'message':'User records has successfully been deleted from the database'},HTTPStatus.OK