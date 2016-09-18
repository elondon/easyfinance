from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.database import session
from app.domain.models import User


def create_user(register_request):
    user = User(username=register_request.username, first_name=register_request.first_name,
                last_name=register_request.last_name, email=register_request.email)
    user.hash_password(register_request.password)

    session.add(user)
    session.commit()
    return user


def get_user(user_request, id):
    user = session.query(User).get(id)
    return user
