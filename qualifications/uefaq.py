from .uefastates import startstate
import qualifications.qualinterface as qual

class Uefa(qual.Qualification):

    """docstring for Uefa."""

    def __init__(self, simulator, teams):
        global state
        state = startstate.Startstate(teams)
        super(Uefa, self).__init__(simulator, teams)

    def next():
        pass
