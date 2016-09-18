from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.database import session
from app.domain.models import *


# users
def create_user(register_request):
    user = User(username=register_request.username, first_name=register_request.first_name,
                last_name=register_request.last_name, email=register_request.email)
    user.hash_password(register_request.password)

    session.add(user)
    session.commit()
    return user


def get_user(user_id):
    user = session.query(User).get(user_id)
    return user


# entities
def create_entity(entity_request, user_id):
    entity = Entity(name=entity_request.name, description=entity_request.description, user_id=user_id)
    session.add(entity)
    session.commit()
    return entity


def get_entity(entity_id):
    entity = session.query(Entity).get(entity_id)
    return entity


def update_entity(entity_request, entity_id):
    entity = session.query(Entity).get(entity_id)
    entity.name = entity_request.name
    entity.description = entity_request.description
    session.commit()
    return entity


# revenue
def create_revenue(revenue_request, entity_id):
    revenue = Revenue(name=revenue_request.name, description=revenue_request.description, value=revenue_request.value,
                      entity_id=entity_id)
    session.add(revenue)
    session.commit()
    return revenue


def get_revenue(revenue_id):
    revenue = session.query(Revenue).get(revenue_id)
    return revenue


def update_revenue(revenue_request, revenue_id):
    revenue = session.query(Revenue).get(revenue_id)
    revenue.name = revenue_request.name
    revenue.description = revenue_request.description
    revenue.value = revenue_request.value
    session.commit()
    return revenue


# cost
def create_cost(cost_request, entity_id):
    cost = Cost(name=cost_request.name, description=cost_request.description, value=cost_request.value,
                entity_id=entity_id)
    session.add(cost)
    session.commit()
    return cost


def get_cost(cost_id):
    cost = session.query(Cost).get(cost_id)
    return cost


def update_cost(cost_request, cost_id):
    cost = session.query(Cost).get(cost_id)
    cost.name = cost_request.name
    cost.description = cost_request.description
    cost.value = cost_request.value
    session.commit()
    return cost


# operatingexpense
def create_operatingexpense(operatingexpense_request, entity_id):
    operatingexpense = OperatingExpense(name=operatingexpense_request.name,
                                        description=operatingexpense_request.description,
                                        value=operatingexpense_request.value,
                                        entity_id=entity_id)
    session.add(operatingexpense)
    session.commit()
    return operatingexpense


def get_operatingexpense(operatingexpense_id):
    operatingexpense = session.query(OperatingExpense).get(operatingexpense_id)
    return operatingexpense


def update_operatingexpense(operatingexpense_request, operatingexpense_id):
    operatingexpense = session.query(OperatingExpense).get(operatingexpense_id)
    operatingexpense.name = operatingexpense_request.name
    operatingexpense.description = operatingexpense_request.description
    operatingexpense.value = operatingexpense_request.value
    session.commit()
    return operatingexpense
