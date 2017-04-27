class QualificationState(object):

    def __init__(self, board, simulator):
        self.board = board
        self.simulator = simulator

        self.ended = False
        self.team_a = 0
        self.team_b = 1

        super(QualificationState, self).__init__()

    def print_board(self):
        for group in self.board:
            for j in group:
                print(str(j), end='\n')
            print('\n')

    def next(self):
        if(self.ended):
            printf('UEFA kvalifikácia sa skončila')
        else:

            for b in self.board:
                self.simulator.simulate(b, self.team_a, self.team_b, 'UEFA')
            self.print_board()

            self.team_b += 1
            if(self.team_b > 5):
                self.team_a += 1
                self.team_b = self.team_a +1

            if(self.team_b > 5):
                self.ended = True
                print('Koniec kvalifikácie.')

        return self

    def has_next(self):
        return not self.ended

    def get_winners(self):
        #Vrátime list tímov, ktoré postúpili na majstrovstvá sveta
        winners = []
        for b in self.board:
            winners.append(b[0]['name'])
        #Rusko patrí do UEFA a rusko je host majstrovstiev
        winners.append('Russia')

        return winners
    def print_table(self):
        self.print_board()
