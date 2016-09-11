import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = flask.current_app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    username = db.Column(db.String(150))
    password = db.Column(db.String(250))


class Entity(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))

    revenue = relationship("Revenue")
    costs = relationship("Cost")
    operating_expenses = relationship("OperatingExpense")


class Revenue(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, ForeignKey('entity.id'))
    name = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Unicode)
    value = db.Column(db.Float, nullable=False)


class Cost(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, ForeignKey('entity.id'))
    name = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Unicode)
    value = db.Column(db.Float, nullable=False)


class OperatingExpense(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    entity_id = db.Column(db.BigInteger, ForeignKey('entity.id'))
    name = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Unicode)
    value = db.Column(db.Float, nullable=False)
