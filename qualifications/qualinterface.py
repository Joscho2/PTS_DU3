class Qualification(object):

    """Abstraktná trieda pre všetky kvalifikácie."""

    def next(self):
        """Odsimulovanie nasledujúceho dňa"""

        raise NotImplementedError( 'Should have implemented this' )

    def has_next(self):
        """Či sa ešte kvalifikácia neskončila. (či existuje ďalší deň)"""

        raise NotImplementedError( 'Should have implemented this' )

    def get_winners(self):
        """Vrátenie víťazov kvalifikácie"""

        raise NotImplementedError( 'Should have implemented this' )

    def print_table(self):
        """Vypísanie tabuľky zápasov na stdout"""

        raise NotImplementedError( 'Should have implemented this' )
