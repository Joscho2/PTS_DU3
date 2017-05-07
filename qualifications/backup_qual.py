import random
import qualifications.qualinterface as qual

class Backup(qual.Qualification):
    """Doplní požadovaný počet tímov"""

    def __init__(self, num_of_teams, teams):
        self.num_of_teams = num_of_teams
        self.teams = teams

    def has_next(self):
        False

    def get_winners(self):
        
        """Náhodne vyberie zo 'záložnej'
        kvalifikácie self.num_of_teams tímov."""

        random.shuffle(self.teams)
        winners = []

        for t in range(0, self.num_of_teams):
            winners.append(self.teams[t][0])

        return winners

    def print_table(self):
        pass
