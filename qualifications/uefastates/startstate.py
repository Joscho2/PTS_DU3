import math
import qualifications.uefastates.qualificationstate as qs

class Startstate(object):
    """UEFA - počiatočný stav. Tu sa udeje vygenerovanie tabuľky"""

    board = [] #List skupin, skupina je list timov, tim je slovnik

    def __init__(self, teams, simulator):

        """Konštruktor, v ktorom sa deje rozdelenie týmov
        do tabuliek ktoré budú všetky pod 'self.board'"""


        counter = 0

        #Potichu predpokladáme počet tímov deliteľný 6.
        #Zmenenie by sa týkalo iba tejto funkcie
        max_count = len(teams)/6;

        for i in range(0, math.ceil(max_count)):
            self.board.append([])

        #Rozlosovanie nie je zrovna náhodné, ale tiež je to len
        #vecou zmeny tohto kúsku kódu
        for i in sorted(teams, key=lambda x: x[1], reverse = True):
            self.board[counter].append({'name' : i[0], 'won': 0, 'score' : 0})
            counter += 1
            if(counter == max_count): counter = 0

        self.simulator = simulator

    def next(self):

        """Malo by byť zavolané iba raz. Vrátime nový stav,
        kde sa už budú konať zápasy, dáme mu vygenerovanú tabuľku."""

        for group in self.board:
            for j in group:
                print(str(j), end='\n')
            print('\n')

        return qs.QualificationState(self.board, self.simulator)

    def has_next(self):
        return True

    def print_table(self):

        """Výpis vygenerovaných tabuliek."""

        for group in self.board:
            for j in group:
                print(str(j), end='\n')
            print('\n')
