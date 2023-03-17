
from ..utils import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id =db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(50), nullable=False,unique=True)
    username=db.Column(db.String(50), nullable=False,unique=True)
    user_type = db.Column(db.String(15))
    email =db.Column(db.String(50), nullable=False,unique=True)
    password_hash =db.Column(db.Text(), nullable=False)
  
    

    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }

    
    def __repr__(self):
        return f"<User {self.username}>"

  
    #Add new user every time a request is mad
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
#Admin table
class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    

#Student
class Student(User):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    score = db.relationship('Score', backref="student_score", lazy=True)
    course=db.relationship('Course', secondary='student_course',lazy=True)
    matric_no = db.Column(db.String(20),nullable=True)
    
    

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
      
    def update(self):
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


