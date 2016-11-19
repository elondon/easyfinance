from flask import json
from flask import jsonify

from app.models.income_statement import IncomeStatement


def get_revenue_array(revenue_list):
    revenue_json_array = []
    for r in revenue_list:
        revenue_json_array.append({
            'id': r.id,
            'entityId': r.entity_id,
            'unitName': r.unit_name,
            'unitDescription': r.unit_description,
            'unitCost': r.unit_cost,
            'unitCount': r.unit_count
        })
    return revenue_json_array


def get_costs_array(cost_list):
    costs_json_array = []
    for r in cost_list:
        costs_json_array.append({
            'entityId': r.entity_id,
            'id': r.id,
            'name': r.name,
            'description': r.description,
            'value': r.value
        })
    return costs_json_array


def get_operating_expenses_array(opex_list):
    operating_expenses_json_array = []
    for r in opex_list:
        operating_expenses_json_array.append({
            'entityId': r.entity_id,
            'id': r.id,
            'name': r.name,
            'description': r.description,
            'value': r.value
        })
    return operating_expenses_json_array


class RegisterResponse:
    def __init__(self, user):
        self.user = user

    def to_json(self):
        response_dict = {
            'user': {
                'id': self.user.id,
                'email': self.user.email,
                'username': self.user.username,
                'firstName': self.user.first_name,
                'lastName': self.user.last_name
            }
        }
        return jsonify(response_dict)


class UserResponse:
    def __init__(self, user):
        self.user = user

    def to_json(self):
        entity_array = []
        for e in self.user.entities:
            entity_dict = {
                'id': e.id,
                'name': e.name,
                'description': e.description,
                'revenue': get_revenue_array(e.revenue),
                'costs': get_costs_array(e.costs),
                'operatingExpenses': get_operating_expenses_array(e.operating_expenses)
            }
            entity_array.append(entity_dict)

        response_dict = {
            'user': {
                'id': self.user.id,
                'email': self.user.email,
                'username': self.user.username,
                'firstName': self.user.first_name,
                'lastName': self.user.last_name,
                'entities': entity_array
            }
        }
        return jsonify(response_dict)


class UserEntitiesResponse:
    def __init__(self, user):
        self.user = user

    def to_json(self):
        entity_array = []
        for e in self.user.entities:
            entity_dict = {
                'id': e.id,
                'name': e.name,
                'description': e.description,
                'revenue': get_revenue_array(e.revenue),
                'costs': get_costs_array(e.costs),
                'operatingExpenses': get_operating_expenses_array(e.operating_expenses)
            }
            entity_array.append(entity_dict)

        response_dict = {
            'entities': entity_array
        }
        return jsonify(response_dict)


class EntityResponse:
    def __init__(self, entity):
        self.entity = entity

    def to_json(self):
        response_dict = {
            'entity': {
                'id': self.entity.id,
                'name': self.entity.name,
                'description': self.entity.description,
                'revenue': get_revenue_array(self.entity.revenue),
                'costs': get_costs_array(self.entity.costs),
                'operatingExpenses': get_operating_expenses_array(self.entity.operating_expenses)
            }
        }
        return jsonify(response_dict)


class RevenueResponse:
    def __init__(self, revenue):
        self.revenue = revenue

    def to_json(self):
        response_dict = {
            'revenue': {
                'id': self.revenue.id,
                'entityId': self.revenue.entity_id,
                'unitName': self.revenue.unit_name,
                'unitDescription': self.revenue.unit_description,
                'unitCost': self.revenue.unit_cost,
                'unitCount': self.revenue.unit_count
            }
        }
        return jsonify(response_dict)


class RevenueDeletedResponse:
    def __init__(self, revenue_id, entity_id):
        self.revenue_id = revenue_id
        self.entity_id = entity_id

    def to_json(self):
        response_dict = {
            'status': 'DELETED',
            'entityId': self.entity_id,
            'revenueId': self.revenue_id
        }
        return jsonify(response_dict)


class CostDeletedResponse:
    def __init__(self, cost_id, entity_id):
        self.cost_id = cost_id
        self.entity_id = entity_id

    def to_json(self):
        response_dict = {
            'status': 'DELETED',
            'entityId': self.entity_id,
            'costId': self.cost_id
        }
        return jsonify(response_dict)


class CostResponse:
    def __init__(self, cost):
        self.cost = cost

    def to_json(self):
        response_dict = {
            'cost': {
                'entityId': self.cost.entity_id,
                'id': self.cost.id,
                'name': self.cost.name,
                'description': self.cost.description,
                'value': self.cost.value
            }
        }
        return jsonify(response_dict)


class OperatingExpenseResponse:
    def __init__(self, operating_expense):
        self.operating_expense = operating_expense

    def to_json(self):
        response_dict = {
            'operatingExpense': {
                'entityId': self.operating_expense.entity_id,
                'id': self.operating_expense.id,
                'name': self.operating_expense.name,
                'description': self.operating_expense.description,
                'value': self.operating_expense.value
            }
        }
        return jsonify(response_dict)


class IncomeStatementResponse:
    def __init__(self, entity):
        self.entity = entity

    def calculate_and_respond(self):
        income_statement = IncomeStatement(self.entity)
        response_dict = {
            'incomeStatement': {
                'entityId': self.entity.id,
                'totalCosts': income_statement.total_costs,
                'totalCostItems': len(self.entity.costs),
                'totalRevenue': income_statement.total_revenue,
                'totalRevenueItems': len(self.entity.revenue),
                'totalOpex': income_statement.total_opex,
                'totalOpexItems': len(self.entity.operating_expenses),
                'grossProfit': income_statement.gross_profit,
                'ebitda': income_statement.ebitda
            }
        }
        return jsonify(response_dict)
