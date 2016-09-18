import unittest
from unittest import TestCase

from flask import json

from app.easyfinance import app

api_root = '/easyfinance/api/v1'


class UserTest(TestCase):
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



if __name__ == '__main__':
    unittest.main()
