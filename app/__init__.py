import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate() 
login_manager = LoginManager()
login_manager.login_view = "auth.login"
from .models import Employee, Admin

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id)) or Admin.query.get(int(user_id))




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    
    db.init_app(app)
    migrate.init_app(app, db)  # Attach Migrate to app and db
    login_manager.init_app(app)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)
    
    return app
