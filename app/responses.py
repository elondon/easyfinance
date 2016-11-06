from flask import json
from flask import jsonify


def get_revenue_array(revenue_list):
    revenue_json_array = []
    for r in revenue_list:
        revenue_json_array.append({
            'id': r.id,
            'entity_id': r.entity_id,
            'unit_name': r.unit_name,
            'unit_description': r.unit_description,
            'unit_cost': r.unit_cost,
            'unit_count': r.unit_count
        })
    return revenue_json_array


def get_costs_array(cost_list):
    costs_json_array = []
    for r in cost_list:
        costs_json_array.append({
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
                'id': str(self.user.id),
                'email': self.user.email,
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name
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
                'id': str(e.id),
                'name': e.name,
                'description': e.description,
                'revenue': get_revenue_array(e.revenue),
                'costs': get_costs_array(e.costs),
                'operating_expenses': get_operating_expenses_array(e.operating_expenses)
            }
            entity_array.append(entity_dict)

        response_dict = {
            'user': {
                'id': str(self.user.id),
                'email': self.user.email,
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
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
                'id': str(e.id),
                'name': e.name,
                'description': e.description,
                'revenue': get_revenue_array(e.revenue),
                'costs': get_costs_array(e.costs),
                'operating_expenses': get_operating_expenses_array(e.operating_expenses)
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
                'id': str(self.entity.id),
                'name': self.entity.name,
                'description': self.entity.description,
                'revenue': get_revenue_array(self.entity.revenue),
                'costs': get_costs_array(self.entity.costs),
                'operating_expenses': get_operating_expenses_array(self.entity.operating_expenses)
            }
        }
        return jsonify(response_dict)


class RevenueResponse:
    def __init__(self, revenue):
        self.revenue = revenue

    def to_json(self):
        response_dict = {
            'revenue': {
                'id': str(self.revenue.id),
                'entity_id': str(self.revenue.entity_id),
                'name': self.revenue.name,
                'description': self.revenue.description,
                'value': self.revenue.value
            }
        }
        return jsonify(response_dict)


class CostResponse:
    def __init__(self, cost):
        self.cost = cost

    def to_json(self):
        response_dict = {
            'cost': {
                'id': str(self.cost.id),
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
            'operating_expense': {
                'id': str(self.operating_expense.id),
                'name': self.operating_expense.name,
                'description': self.operating_expense.description,
                'value': self.operating_expense.value
            }
        }
        return jsonify(response_dict)
