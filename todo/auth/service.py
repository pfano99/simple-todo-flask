from flask_login import login_user, logout_user

from todo import bcrypt, oauth
from todo.secrets import google_auth
from todo.user.service import find_user_by_email, add_user


def _login_user(email: str, password: str):
    user = find_user_by_email(email=email)
    if user:
        if password:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
        else:
            login_user(user)


def _logout_user():
    logout_user()


def google_login(redirect_uri: str):
    conf_url = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=google_auth.get("client_id"),
        client_secret=google_auth.get("client_secret"),
        server_metadata_url=conf_url,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    return oauth.google.authorize_redirect(redirect_uri)


def google_login_response():
    token = oauth.google.authorize_access_token()

    if token["userinfo"]["email_verified"]:
        user = find_user_by_email(email=token["userinfo"]["email"])
        if not user:
            add_user(first_name=token["userinfo"]["given_name"], last_name=token["userinfo"]["family_name"],
                     email=token["userinfo"]["email"], password=None, auth_type="google"
                     )
        _login_user(email=token["userinfo"]["email"], password=None)
    else:
        pass
