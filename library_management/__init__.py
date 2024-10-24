# from flask import Flask
# from flask_mysqldb import MySQL
# from config.config import Config 
# from library_management.routes import book_routes

# mysql = MySQL()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     mysql.init_app(app)
#     app.register_blueprint(book_routes.bp)
#     # app.register_blueprint(member_routes.bp)
#     # app.register_blueprint(transaction_routes.bp)

#     return app