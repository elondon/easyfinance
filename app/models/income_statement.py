from app.models.model import Model


class IncomeStatement(Model):

    @property
    def gross_profit(self):
        revenue = sum(x.value + x.value for x in self.entity.revenue)
        costs = sum(x.value + x.value for x in self.entity.costs)
        return revenue + costs

    @property
    def ebitda(self):
        opex = sum(x.value + x.value for x in self.entity.operating_expenses)
        return opex + self.gross_profit
