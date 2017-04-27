class Qualification(object):

    """Abstraktná trieda pre všetky kvalifikácie."""

    teams = []

    def __init__(self, simulator, teams):
        """Nastaví zvolený simulátor zápasov"""

        self.simulator = simulator
        self.team = teams

    def next(self):
        """Odsimulovanie nasledujúceho dňa"""

        raise NotImplementedError( "Should have implemented this" )
