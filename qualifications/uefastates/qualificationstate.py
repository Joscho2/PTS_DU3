class QualificationState(object):

    """Stav UEFA kvalifikácie,
    v ktorom sa už po dostatní vylosovanej
    tabuľky deje odohrávanie zápasov."""

    def __init__(self, board, simulator):

        """Konštruktor, spracovanie tabuľky."""

        self.board = board
        self.simulator = simulator

        self.ended = False

        #Pripravenie premenných pre simulátor
        self.team_a = 0
        self.team_b = 1

        super(QualificationState, self).__init__()

    def print_board(self):
        """Výpis tabuliek UEFA kvalifikácie."""
        for group in self.board:
            for j in group:
                print(str(j), end='\n')
            print('\n')

    def next(self):

        """Odsimulovanie ďalšieho dňa UEFA kvalifikácie."""

        if(self.ended):
            print('UEFA kvalifikácia sa skončila')
        else:

            for b in self.board:
                #V každej tabuľke odohrá každý s každým
                self.simulator.simulate(b, self.team_a, self.team_b, 'UEFA')

            self.print_board()

            #Len inkrementovanie premenných pre to aby
            #hral každý s každým
            self.team_b += 1
            if(self.team_b > 5):
                self.team_a += 1
                self.team_b = self.team_a +1

            if(self.team_b > 5):
                self.ended = True
                print('Koniec kvalifikácie UEFA.')

        return self

    def has_next(self):
        """Či existuje zápas na odohranie."""
        return not self.ended

    def get_winners(self):
        #Vrátime list tímov, ktoré postúpili na majstrovstvá sveta
        winners = []
        for b in self.board:
            winners.append(sorted(b, key = lambda team:team['score'], reverse=True)[0]['name'])
        #Rusko patrí do UEFA a Rusko je host majstrovstiev
        winners.append('Russia')

        return winners

    def print_table(self):
        """Zobrazenie tabuliek kvalifikácie.
        Definované interfaceom."""
        self.print_board()
