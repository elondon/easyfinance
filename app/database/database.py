from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
some_engine = create_engine('postgresql://svceasyfinance:welcome@localhost/easyfinance')
session_maker = sessionmaker(some_engine)
session = session_maker()


def init_db(app):
    db.init_app(app)
    global some_engine
    global session_maker
    global session
    some_engine = create_engine('postgresql://svceasyfinance:welcome@localhost/easyfinance')
    session_maker = sessionmaker(some_engine)
    session = session_maker()
