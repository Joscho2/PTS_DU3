class Final(object):

    """docstring for Final."""

    def __init__(self, teams, simulator):
        if(len(teams) != 32):
            print('Tímov sa má dostať do finálne 32! .. nie ' + str(len(teams)), end = '\n')
            exit()

        self.teams = teams
        self.simulator = simulator
        print('Tými začínajúce vo finále: ' + str(teams), end='\n')
        super(Final, self).__init__()

    def has_next(self):
        if(len(self.teams) == 1):
            return False
        else:
            return True

    def next(self):
        win_teams = []

        teams = self.teams
        for t in range(0, len(teams), 2):
            comment = 'World Cup'
            if(len(teams) == 2): comment = '>>Final<<'

            win_teams.append(self.simulator.simulate_final(teams[t], teams[t+1], comment))

        self.teams = win_teams
        print('Postúpili: ' + str(self.teams), end = '\n')
