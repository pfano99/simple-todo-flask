from todo import bcrypt, db
from todo.auth.repository import find_auth_type_by_name
from todo.models import User


def add_user(first_name: str, last_name: str, email: str, password: str, auth_type_name: str) -> bool:
    auth_type = find_auth_type_by_name(auth_type_name)
    if password:
        password = bcrypt.generate_password_hash(password)
    user = User(first_name=first_name, last_name=last_name, email=email, password=password,
                auth_type=auth_type.id)
    db.session.add(user)
    db.session.commit()
    return True


def find_user_by_id(user_id: int) -> User:
    return User.query.get(user_id)


def find_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()
