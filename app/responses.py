class RegisterResponse:
    def __init__(self, user):
        self.id = user.id
        self.username = user.user_name
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
