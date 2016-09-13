import flask
from flask.ext.sqlalchemy import SQLAlchemy

from app.domain.models import User

app = flask.current_app
db = SQLAlchemy(app)


def create_user(register_request):
    user = User(username=register_request.user_name, first_name=register_request.first_name,
                last_name=register_request.last_name, email=register_request.email)
    user.hash_password(register_request.password)

    
