import json
import logging
import os

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from http.client import HTTPException
from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import abort, default_exceptions

from app.database.database import init_db
from app.database.repository import *
from app.requests import RegisterRequest
from app.responses import RegisterResponse

path = os.path.dirname(os.path.abspath(__file__))
api_root = '/easyfinance/api/v1'


def make_json_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code
                            if isinstance(ex, HTTPException)
                            else 500)
    return response

app = Flask(__name__)
cors = CORS(app, resources={r"/easyfinance/api/v1/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://svceasyfinance:welcome@localhost/easyfinance'

init_db(app)

# make all errors return json.
for code in default_exceptions.keys():
    app.error_handler_spec[None][code] = make_json_error

# logging
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler(path + '/access.log')

if app.debug is True:
    app.logger.setLevel(logging.DEBUG)
    logging.getLogger().setLevel(logging.DEBUG)

    logger.addHandler(handler)
    app.logger.addHandler(handler)
else:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    logging.getLogger().setLevel(logging.INFO)


# authentication end points
@app.route(api_root + '/auth/register', methods=['POST'])
def route_auth_register():
    register_request = RegisterRequest(request=request)
    user = create_user(register_request)
    response = RegisterResponse(user=user)
    return jsonify(response)


@app.route(api_root + '/auth/login', methods=['POST'])
def route_auth_login():
    pass


# user end points.
@app.route(api_root + '/user/<user_id>', methods=['GET'])
def route_get_user(user_id):
    user = get_user(user_id)
    return jsonify(vars(user))


# entity end points. entity is an aggregate root.
# entities are business entities or individuals.
# entities store data that models can run against.
@app.route(api_root + '/entity/<entity_id>', methods=['GET'])
def entity_get(entity_id):
    pass


@app.route(api_root + '/entity', methods=['POST'])
def entity_create():
    pass


@app.route(api_root + '/entity/<entity_id>', methods=['PUT'])
def entity_update(entity_id):
    pass


@app.route(api_root + '/entity/<entity_id>', methods=['DELETE'])
def entity_delete(entity_id):
    pass


# revenue end points. handles an entities revenue items.
@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['GET'])
def revenue_get(entity_id, revenue_id):
    pass


@app.route(api_root + '/entity/<entity_id>/revenue', methods=['POST'])
def revenue_create(entity_id):
    pass


@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['PUT'])
def revenue_update(entity_id, revenue_id):
    pass


@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['DELETE'])
def revenue_delete(entity_id, revenue_id):
    pass


# cost end points. handles an entities cost items.
@app.route(api_root + '/entity/<entity_id>/cost/<cost_id>', methods=['GET'])
def cost_get(entity_id, cost_id):
    pass


@app.route(api_root + '/entity/<entity_id>/cost', methods=['POST'])
def cost_create(entity_id):
    pass


@app.route(api_root + '/entity/<entity_id>/cost/<cost_id>', methods=['PUT'])
def cost_update(entity_id, cost_id):
    pass


@app.route(api_root + '/entity/<entity_id>/cost/<cost_id>', methods=['DELETE'])
def cost_delete(entity_id, cost_id):
    pass


# opex end points. handles an entities operating expense items.
@app.route(api_root + '/entity/<entity_id>/opex/<opex_id>', methods=['GET'])
def opex_get(entity_id, opex_id):
    pass


@app.route(api_root + '/entity/<entity_id>/opex', methods=['POST'])
def opex_create(entity_id):
    pass


@app.route(api_root + '/entity/<entity_id>/opex/<opex_id>', methods=['PUT'])
def opex_update(entity_id, opex_id):
    pass


@app.route(api_root + '/entity/<entity_id>/opex/<opex_id>', methods=['DELETE'])
def opex_delete(entity_id, opex_id):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', passthrough_errors=True)
