import json
import logging
import os

from flask import Response
from flask_cors import CORS
from http.client import HTTPException
from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import abort, default_exceptions

from app.database.database import init_db
from app.database.repository import *

from app.objectview import ObjectView
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
    json_request = request.get_json()
    register_request = ObjectView(json_request)
    user = create_user(register_request)
    response = RegisterResponse(user=user)
    return response.to_json()


@app.route(api_root + '/auth/login', methods=['POST'])
def route_auth_login():
    json_request = request.get_json()
    login_request = ObjectView(json_request)
    user = login(login_request)
    response = UserResponse(user=user)
    return response.to_json()


# user end points.
@app.route(api_root + '/user/<user_id>', methods=['GET'])
def route_get_user(user_id):
    user = get_user(user_id)
    response = UserResponse(user=user)
    return response.to_json()


@app.route(api_root + '/user/<user_id>/entities', methods=['GET'])
def route_get_user_entities(user_id):
    user = get_user(user_id)
    response = UserEntitiesResponse(user=user)
    return response.to_json()


# entity endpoints
@app.route(api_root + '/entity/<entity_id>', methods=['GET'])
def entity_get(entity_id):
    entity = get_entity(entity_id=entity_id)
    response = EntityResponse(entity=entity)
    return response.to_json()


@app.route(api_root + '/<user_id>/entity', methods=['POST'])
def entity_create(user_id):
    json_request = request.get_json()
    entity_request = ObjectView(json_request)
    entity = create_entity(entity_request=entity_request, user_id=user_id)
    response = EntityResponse(entity=entity)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>', methods=['PUT'])
def entity_update(entity_id):
    json_request = request.get_json()
    entity_request = ObjectView(json_request)
    entity = update_entity(entity_request=entity_request, entity_id=entity_id)
    response = EntityResponse(entity=entity)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>', methods=['DELETE'])
def entity_delete(entity_id):
    pass


# financial model end points
@app.route(api_root + '/entity/<entity_id>/incomestatement', methods=['GET'])
def income_statement(entity_id):
    entity = get_entity(entity_id=entity_id)
    response = IncomeStatementResponse(entity=entity)
    return response.calculate_and_respond()


# revenue end points. handles an entities revenue items.
@app.route(api_root + '/revenue/<revenue_id>', methods=['GET'])
def revenue_get(revenue_id):
    revenue = get_revenue(revenue_id=revenue_id)
    response = RevenueResponse(revenue)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/revenue', methods=['POST'])
def revenue_create(entity_id):
    json_request = request.get_json()
    revenue_request = ObjectView(json_request)
    revenue = create_revenue(revenue_request=revenue_request, entity_id=entity_id)
    response = RevenueResponse(revenue)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['PUT'])
def revenue_update(entity_id, revenue_id):
    json_request = request.get_json()
    revenue_request = ObjectView(json_request)
    revenue = update_revenue(revenue_request=revenue_request, revenue_id=revenue_id)
    response = RevenueResponse(revenue)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/revenue/<revenue_id>', methods=['DELETE'])
def revenue_delete(entity_id, revenue_id):
    delete_revenue(int(revenue_id))
    response = RevenueDeletedResponse(int(revenue_id), int(entity_id))
    return response.to_json()


# cost end points. handles an entities cost items.
@app.route(api_root + '/cost/<cost_id>', methods=['GET'])
def cost_get(cost_id):
    cost = get_cost(cost_id=cost_id)
    response = CostResponse(cost)
    return response.to_json()


@app.route(api_root + '/entity/<entity_id>/cost', methods=['POST'])
def cost_create(entity_id):
    json_request = request.get_json()
    cost_request = ObjectView(json_request)
    cost = create_cost(cost_request=cost_request, entity_id=entity_id)
    cost_response = CostResponse(cost=cost)
    return cost_response.to_json()


@app.route(api_root + '/entity/<entity_id>/cost/<cost_id>', methods=['PUT'])
def cost_update(entity_id, cost_id):
    json_request = request.get_json()
    cost_request = ObjectView(json_request)
    cost = update_cost(cost_request=cost_request, cost_id=cost_id)
    cost_response = CostResponse(cost=cost)
    return cost_response.to_json()


@app.route(api_root + '/entity/<entity_id>/cost/<cost_id>', methods=['DELETE'])
def cost_delete(entity_id, cost_id):
    delete_cost(int(cost_id))
    response = CostDeletedResponse(int(cost_id), int(entity_id))
    return response.to_json()


# opex end points. handles an entities operating expense items.
@app.route(api_root + '/opex/<opex_id>', methods=['GET'])
def opex_get(opex_id):
    opex = get_operatingexpense(operatingexpense_id=opex_id)
    opex_response = OperatingExpenseResponse(operating_expense=opex)
    return opex_response.to_json()


@app.route(api_root + '/entity/<entity_id>/opex', methods=['POST'])
def opex_create(entity_id):
    json_request = request.get_json()
    opex_request = ObjectView(json_request)
    opex = create_operatingexpense(operatingexpense_request=opex_request, entity_id=entity_id)
    opex_response = OperatingExpenseResponse(opex)
    return opex_response.to_json()


@app.route(api_root + '/opex/<opex_id>', methods=['PUT'])
def opex_update(opex_id):
    json_request = request.get_json()
    opex_request = ObjectView(json_request)
    opex = update_operatingexpense(operatingexpense_request=opex_request, operatingexpense_id=opex_id)
    opex_response = OperatingExpenseResponse(opex)
    return opex_response.to_json()


@app.route(api_root + '/entity/<entity_id>/opex/<opex_id>', methods=['DELETE'])
def opex_delete(entity_id, opex_id):
    delete_opex(int(opex_id))
    response = OpexDeletedResponse(int(opex_id), int(entity_id))
    return response.to_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', passthrough_errors=True)
