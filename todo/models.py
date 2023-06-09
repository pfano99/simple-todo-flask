import datetime

from flask_login import UserMixin
from todo import db

from todo import login_manager


@login_manager.user_loader
def load_user(_id):
    return User.query.get(_id)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    password = db.Column(db.String(50), nullable=True, default=None)

    task = db.relationship('Task', backref='user', lazy=True, cascade="all, delete-orphan")
    auth_type_id = db.Column(db.Integer, db.ForeignKey('auth_type.id'))

    def __repr__(self):
        return "User( id: {}, first-name: {}, last-name: {}, email: {}, auth_type_id: {})".format(
            self.id, self.first_name, self.last_name, self.email, self.auth_type_id
        )


class AuthType(db.Model):
    __tablename__ = "auth_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("type", db.String)  # Default, Google, Twitter, Facebook, Github
    users = db.relationship('User', backref='auth_type', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return "Auth-Type( id: {}, name: {} )".format(self.id, self.name)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='')
    description = db.Column(db.Text, nullable=False)
    finish_by = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "Task ( id: {}, name: {}, status: {}, description: {}, finish_by: {}".format(
            self.id, self.name, self.status, self.description, self.finish_by
        )
