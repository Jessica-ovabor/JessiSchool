import os
from decouple import config
from datetime import timedelta



BASE_DIR = os.path.dirname(os.path.realpath(__file__))
class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    #sql alchemy secret key development stage   
class DevConfig(Config):
    DEBUG = config('DEBUG',cast=bool)    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    SQLALCHEMY_ECHO =True#allows us to view our db in sql forrmat
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
class TestConfig(Config):
    TESTING =True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO =True#allows us to view our db in sql forrmat
    SQLALCHEMY_DATABASE_URI= 'sqlite://'#using  the memory database that is why there no path and 2 forward slash

class ProdConfig(Config):
    pass
# so we can use it this in our init.py
config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test': TestConfig
}                                                                       