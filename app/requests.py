class RegisterRequest:
    def __init__(self, request):
        self.username = request.args.get('username')
        self.first_name = request.args.get('first_name')
        self.last_name = request.args.get('last_name')
        self.email = request.args.get('email')
        self.password = request.args.get('password')


class EntityRequest:
    def __init__(self, request):
        self.id = request.args.get('id')
        self.name = request.args.get('name')
        self.description = request.args.get('description')


class RevenueRequest:
    def __init__(self, request):
        self.id = request.args.get('id')
        self.name = request.args.get('name')
        self.description = request.args.get('description')
        self.value = request.args.get('value')


class CostRequest:
    def __init__(self, request):
        self.id = request.args.get('id')
        self.name = request.args.get('name')
        self.description = request.args.get('description')
        self.value = request.args.get('value')


class OperatingExpenseRequest:
    def __init__(self, request):
        self.id = request.args.get('id')
        self.name = request.args.get('name')
        self.description = request.args.get('description')
        self.value = request.args.get('value')
