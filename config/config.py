import os
from flask_mysqldb import MySQL
class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'lms'
    SECRET_KEY = os.urandom(24)
    
# def connectDB():
#     mysql = MySQL()
#     mysql.init_app(Config)