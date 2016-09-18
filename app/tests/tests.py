import unittest
from unittest import TestCase

from app.easyfinance import app

api_root = '/easyfinance/api/v1'


class UserTest(TestCase):
    def test_user_can_register(self):
        tester = app.test_client()
        response = tester.post(
            api_root + '/auth/register?username=test&first_name=test&last_name=test&email=test&password=test')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
