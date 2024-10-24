from flask_mysqldb import MySQL
from config.config import Config
from app import app

import os
class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'lms'
    SECRET_KEY = os.urandom(24)
    

mysql = MySQL()
app.config.from_object(Config)
mysql.init_app(app)
