import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

# todo sqlalchemy defines all data models in one file. After enough business logic is added
# todo this file will become huge. Whats the best way of separating this into manageable pieces
# todo without running into cyclic import issues? Potentially a good use case for a mixin.
from app.database.database import db

app = flask.current_app


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    username = db.Column(db.String(150))
    password = db.Column(db.String(250))
    email = db.Column(db.String(250))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    entities = relationship("Entity")

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=3600):
        s = Serializer('55b82c506d568b0d96315a62dca0a4c8', expires_in=expiration)
        return s.dumps({'id': str(self.id)})

    @staticmethod
    def get_user_for_auth_token(token):
        s = Serializer('55b82c506d568b0d96315a62dca0a4c8')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return False  # valid token, but expired
        except BadSignature:
            return False  # invalid token
        user_id = data['id']
        return user_id


class Entity(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, ForeignKey('user.id'))
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    revenue = relationship("Revenue")
    costs = relationship("Cost")
    operating_expenses = relationship("OperatingExpense")


class Revenue(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, ForeignKey('entity.id'))
    name = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Unicode)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class Cost(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, ForeignKey('entity.id'))
    name = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Unicode)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class OperatingExpense(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, ForeignKey('entity.id'))
    name = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Unicode)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
