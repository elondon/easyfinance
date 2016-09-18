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
from app.requests import *
from app.responses import *

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
    return response.to_json()


@app.route(api_root + '/auth/login', methods=['POST'])
def route_auth_login():
    pass


# user end points.
@app.route(api_root + '/user/<user_id>', methods=['GET'])
def route_get_user(user_id):
    user = get_user(user_id)
    response = RegisterResponse(user=user)
    return response.to_json()


# entities are business entities or individuals.
# entities store data that models can run against.
@app.route(api_root + '/<user_id>/entity/<entity_id>', methods=['GET'])
def entity_get(entity_id):
    entity = get_entity(entity_id=entity_id)
    response = EntityResponse(entity=entity)
    return response.to_json()


@app.route(api_root + '/<user_id>/entity', methods=['POST'])
def entity_create(user_id):
    entity_request = EntityRequest(request=request)
    entity = create_entity(entity_request=entity_request, user_id=user_id)
    response = EntityResponse(entity=entity)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>', methods=['PUT'])
def entity_update(entity_id):
    entity_request = EntityRequest(request=request)
    entity = update_entity(entity_request=entity_request, entity_id=entity_id)
    response = EntityResponse(entity=entity)
    return response.to_json()


@app.route(api_root + '/<user_id>/entity/<entity_id>', methods=['DELETE'])
def entity_delete(user_id, entity_id):
    pass


# revenue end points. handles an entities revenue items.
@app.route(api_root + '/revenue/<revenue_id>', methods=['GET'])
def revenue_get(revenue_id):
    revenue = get_revenue(revenue_id=revenue_id)
    response = RevenueResponse(revenue)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/revenue', methods=['POST'])
def revenue_create(entity_id):
    revenue_request = RevenueRequest(request=request)
    revenue = create_revenue(revenue_request=revenue_request, entity_id=entity_id)
    response = RevenueResponse(revenue)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['PUT'])
def revenue_update(revenue_id):
    revenue_request = RevenueRequest(request=request)
    revenue = update_revenue(revenue_request=revenue_request, revenue_id=revenue_id)
    response = RevenueResponse(revenue)
    return response.to_json()



@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['DELETE'])
def revenue_delete(entity_id, revenue_id):
    pass


# cost end points. handles an entities cost items.
@app.route(api_root + '/cost/<cost_id>', methods=['GET'])
def cost_get(cost_id):
    cost = get_cost(cost_id=cost_id)
    response = CostResponse(cost)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/cost', methods=['POST'])
def cost_create(entity_id):
    cost_request = CostRequest(request=request)
    cost = create_cost(cost_request=cost_request, entity_id=entity_id)
    cost_response = CostResponse(cost=cost)
    return cost_response.to_json()


@app.route(api_root + '/cost/<cost_id>', methods=['PUT'])
def cost_update(cost_id):
    cost_request = CostRequest(request=request)
    cost = update_cost(cost_request=cost_request, cost_id=cost_id)
    cost_response = CostResponse(cost=cost)
    return cost_response.to_json()


@app.route(api_root + '/entity/<entity_id>/cost/<cost_id>', methods=['DELETE'])
def cost_delete(entity_id, cost_id):
    pass


# opex end points. handles an entities operating expense items.
@app.route(api_root + '/opex/<opex_id>', methods=['GET'])
def opex_get(opex_id):
    opex = get_operatingexpense(operatingexpense_id=opex_id)
    opex_response = OperatingExpenseResponse(operating_expense=opex)
    return opex_response.to_json()

@app.route(api_root + '/entity/<entity_id>/opex', methods=['POST'])
def opex_create(entity_id):
    opex_request = OperatingExpenseRequest(request=request)
    opex = create_operatingexpense(operatingexpense_request=opex_request, entity_id=entity_id)
    opex_response = OperatingExpenseResponse(opex)
    return opex_response.to_json()


@app.route(api_root + '/opex/<opex_id>', methods=['PUT'])
def opex_update(opex_id):
    opex_request = OperatingExpenseRequest(request=request)
    opex = update_operatingexpense(operatingexpense_request=opex_request, operatingexpense_id=opex_id)
    opex_response = OperatingExpenseResponse(opex)
    return opex_response.to_json()


@app.route(api_root + '/entity/<entity_id>/opex/<opex_id>', methods=['DELETE'])
def opex_delete(entity_id, opex_id):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', passthrough_errors=True)
