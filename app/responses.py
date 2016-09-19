from flask import json
from flask import jsonify


def get_revenue_array(revenue_list):
    revenue_json_array = []
    for r in revenue_list:
        revenue_json_array.append({
            'id': r.id,
            'name': r.name,
            'description': r.description,
            'value': r.value
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
        self.id = user.id
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email

    def to_json(self):
        response_dict = {
            'user': {
                'id': str(self.id),
                'email': self.email,
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name
            }
        }
        return jsonify(response_dict)


class UserResponse:
    def __init__(self, user):
        self.user = user
        self.id = user.id
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email

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
                'id': str(self.id),
                'email': self.email,
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'entities': entity_array
            }
        }
        return jsonify(response_dict)


class EntityResponse:
    def __init__(self, entity):
        self.id = entity.id
        self.name = entity.name
        self.description = entity.description
        self.revenue = entity.revenue
        self.costs = entity.costs
        self.operating_expenses = entity.operating_expenses

    def to_json(self):
        response_dict = {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'revenue': get_revenue_array(self.revenue),
            'costs': get_costs_array(self.costs),
            'operating_expenses': get_operating_expenses_array(self.operating_expenses)
        }
        return jsonify(response_dict)


class RevenueResponse:
    def __init__(self, revenue):
        self.id = revenue.id
        self.name = revenue.name
        self.description = revenue.description
        self.value = revenue.value

    def to_json(self):
        response_dict = {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'value': self.value
        }
        return jsonify(response_dict)


class CostResponse:
    def __init__(self, cost):
        self.id = cost.id
        self.name = cost.name
        self.description = cost.description
        self.value = cost.value

    def to_json(self):
        response_dict = {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'value': self.value
        }
        return jsonify(response_dict)


class OperatingExpenseResponse:
    def __init__(self, operating_expense):
        self.id = operating_expense.id
        self.name = operating_expense.name
        self.description = operating_expense.description
        self.value = operating_expense.value

    def to_json(self):
        response_dict = {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'value': self.value
        }
        return jsonify(response_dict)
