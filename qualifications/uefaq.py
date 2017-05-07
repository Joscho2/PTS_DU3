from .uefastates import startstate
import qualifications.qualinterface as qual

class Uefa(qual.Qualification):

    """Implementácia UEFA kavlifikácie. Udržuje si stav v akom sa nachádza.
    Samostný stav má nejakú funkcionalitu a on vracia nový stav (alebo sám seba)."""

    def __init__(self, simulator, teams):
        self.state = startstate.Startstate(teams, simulator)

    def next(self):
        self.state = self.state.next()

    def has_next(self):
        return self.state.has_next()

    def get_winners(self):
        return self.state.get_winners()

    def print_table(self):
        self.state.print_table()
