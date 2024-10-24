from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from library_management.routes import book_routes
from config.config import Config

# Initialize MySQL
mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    app.register_blueprint(book_routes.bp, url_prefix='/books')
    CORS(app)
    return app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
