from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config['SECRET_KEY'] = 'THISISTHEKEY'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from todo.main.routes import main
from todo.auth.routes import auth
from todo.user.routes import user
from todo.task.routes import task

app.register_blueprint(main)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(task, url_prefix="/task")

from todo.models import *
