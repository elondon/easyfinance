from flask import jsonify


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
