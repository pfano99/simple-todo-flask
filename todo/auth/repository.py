from todo.models import AuthType


def find_auth_type_by_name(name: str) -> AuthType:
    return AuthType.query.filter_by(name=name).first()
