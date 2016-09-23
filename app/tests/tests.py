import unittest
from unittest import TestCase

from flask import json

from app.database.database import session
from app.domain.models import *
from app.easyfinance import app

api_root = '/easyfinance/api/v1'


class RegisterTest(TestCase):
    def test_user_can_register(self):
        tester = app.test_client()
        response = tester.post(
            api_root + '/auth/register?username=test&first_name=test&last_name=test&email=test&password=test')
        result = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertGreater(int(result['user']['id']), 0)
        self.assertIsNotNone(result['user']['first_name'])
        self.assertIsNotNone(result['user']['last_name'])
        self.assertIsNotNone(result['user']['email'])
        self.assertIsNotNone(result['user']['username'])


class UserTest(TestCase):
    def setUp(self):
        self.tester = app.test_client()
        self.user = User(first_name='Testy', last_name='McTesterson', username='testy', password='test',
                         email='test@testy.com')
        session.add(self.user)
        session.commit()

        self.entity = Entity(name='My Entity', description='My favorite entity', user_id=self.user.id)
        session.add(self.entity)
        session.commit()

        self.revenue = Revenue(name='Revenue 1', description='My First Revenue', value=1, entity_id=self.entity.id)
        self.cost = Cost(name='Cost 1', description='My First Cost', value=1, entity_id=self.entity.id)
        self.opex = OperatingExpense(name='Opex 1', description='My First Opex', value=1, entity_id=self.entity.id)

        session.add(self.revenue)
        session.add(self.cost)
        session.add(self.opex)
        session.commit()

    def test_get_user_with_object_graph(self):
        response = self.tester.get(
            api_root + '/user/%d' % self.user.id,
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))

        self.assertIsNotNone(result['user']['id'])
        self.assertIsNotNone(result['user']['entities'][0]['id'])
        self.assertIsNotNone(result['user']['entities'][0]['revenue'][0]['id'])
        self.assertIsNotNone(result['user']['entities'][0]['operating_expenses'][0]['id'])
        self.assertIsNotNone(result['user']['entities'][0]['costs'][0]['id'])

    def tearDown(self):
        session.delete(self.user)
        session.delete(self.entity)
        session.delete(self.revenue)
        session.delete(self.cost)
        session.delete(self.opex)
        session.commit()


class EntityTest(TestCase):
    def setUp(self):
        self.tester = app.test_client()

        self.user = User(first_name='Testy', last_name='McTesterson', username='testy', password='test',
                         email='test@testy.com')
        session.add(self.user)
        session.commit()

        self.entity = Entity(user_id=self.user.id, name='Test Entity 1', description='This is a test entity')
        session.add(self.entity)
        session.commit()

    def test_get_entity(self):
        response = self.tester.get(
            api_root + '/entity/%d' % self.entity.id,
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(self.entity.id, int(result['entity']['id']))

    def test_create_entity(self):
        response = self.tester.post(
            api_root + '/%u/entity?name=testentity1&description=thisisatestentity' % self.user.id
        )

        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsNotNone(result['entity']['id'])
        self.assertEqual(result['entity']['name'], 'testentity1')

    def test_update_entity(self):
        response = self.tester.put(
            api_root + '/entity/%i?name=updatedentity&description=thisisatestentity' % self.entity.id
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsNotNone(result['entity']['id'])
        self.assertEqual(result['entity']['name'], 'updatedentity')

    def test_delete_entity(self):
        pass

    def test_should_be_able_to_add_reveue(self):
        response = self.tester.post(
            api_root + '/entity/%i/revenue?name=revenue1&description=revenue1&value=5.5' % self.entity.id
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsNotNone(result['revenue']['id'])

    def test_should_be_able_to_add_costs(self):
        response = self.tester.post(
            api_root + '/entity/%i/cost?name=cost1&description=cost1&value=15.5' % self.entity.id
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsNotNone(result['cost']['id'])

    def test_should_be_able_to_add_opex(self):
        response = self.tester.post(
            api_root + '/entity/%i/opex?name=opex&description=opex&value=55.5' % self.entity.id
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIsNotNone(result['operating_expense']['id'])

    def test_should_be_able_to_remove_reveue(self):
        pass

    def test_should_be_able_to_remove_costs(self):
        pass

    def test_should_be_able_to_remove_opex(self):
        pass


    def tearDown(self):
        session.delete(self.user)
        session.delete(self.entity)
        session.commit()


if __name__ == '__main__':
    unittest.main()
