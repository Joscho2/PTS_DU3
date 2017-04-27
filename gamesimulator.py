import random

class GameSimulator(object):
    """docstring for GameSimulator."""

    def __init__(self):
        super(GameSimulator, self).__init__()

    #Prepokladáme, že apoň na úroveň skupín
    #to bude pri každej kvalifikácií
    def simulate(group, team_a, team_b):
        if(random.randint(1) == 0):
            group[team_a]['score'] += 3
        else:
            group[team_b]['score'] += 3
