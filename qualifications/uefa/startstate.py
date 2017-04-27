class Startstate(object):
    """UEFA - počiatočný stav. Tu sa udeje vygenerovanie tabuľky"""


    board = [[{}]] #List skupin, skupina je list timov, tim je slovnik

    def __init__(self, teams):
        counter = 0

        #Potichu predpokladáme počet tímov deliteľný 6.
        #Zmenenie by sa týkalo iba tejto funkcie
        max_count = len(teams)/6;

        #Rozlosovanie nie je zrovna náhodné, ale tiež je to len
        #vecou zmeny tohto kúsku kódu
        for i in sorted(teams, key=lambda x: x[1]):
            board[counter].append({'meno' : i[0], 'vyhral': 0, 'score' : 0})
            if(counter == max_count) counter = 0;

        print(board)

    def next():
        pass
