from app.models.model import Model


class IncomeStatement(Model):

    @property
    def total_costs(self):
        return sum(x.value for x in self.entity.costs)

    @property
    def total_revenue(self):
        return sum(x.unit_count * x.unit_cost for x in self.entity.revenue)

    @property
    def total_opex(self):
        return sum(x.value for x in self.entity.operating_expenses)

    @property
    def gross_profit(self):
        return self.total_revenue - self.total_costs

    @property
    def ebitda(self):
        return self.gross_profit - self.total_opex

