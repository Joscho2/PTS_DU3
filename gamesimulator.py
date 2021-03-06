import random

class GameSimulator(object):
    """Stará sa o výsledky zápasov na ktoré
    zavoláme funkciu simulate - pre kvalifikáciu
    a simulate final pre samotné majstrvostvá."""

    def __init__(self, history):
        self.history = history
        super(GameSimulator, self).__init__()

    #Prepokladáme, že apoň na úroveň skupín
    #to bude pri každej kvalifikácií rovnaké
    def simulate(self, group, team_a, team_b, comment):

        """Simulovanie kvalifikačných zápasov.
        Vylepšenie simulácie zápasov by sa týkali iba
        zmeny tejto funkcie."""

        if(random.randint(0, 1) == 0):
            group[team_a]['score'] += 3
            group[team_a]['won'] += 1
            self.history.add(group[team_a]['name'],
								group[team_b]['name'], comment)
        else:
            group[team_b]['score'] += 3
            group[team_b]['won'] += 1
            self.history.add(group[team_b]['name'],
								group[team_a]['name'], comment)

    def simulate_final(self, team_a, team_b, comment):
        """Simulovanie zápasov na majstrovstvách sveta"""

        if(random.randint(0, 1) == 0):
            self.history.add(team_a, team_b, comment)
            return team_a
        else:
            self.history.add(team_b, team_a, comment)
            return team_b
