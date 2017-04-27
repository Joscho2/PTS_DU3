import final

class GameWrapper(object):
    """Stará sa o správu hry. Oznamuje jednotlivým kvalifikáciam
    posun na nový deň, spracováva postupujúce tími a posúva na nový deň
    aj samotné majstrovstvá."""

    def __init__(self, q_list, simulator, history):
        self.q_list = q_list
        self.qual_is_playing = True
        self.simulator = simulator
        self.history = history
        super(GameWrapper, self).__init__()


    #Odsimulovanie ďalšieho dňa kvalifikácie
    #vráti False ak sa kvalifikácia skončila/ak je škončená
    #inak vráti True
    def q_next(self):
        held = False
        for l in self.q_list:
            if(l.has_next()):
                held = True
                l.next()
        if(not held):
            print('Vstup do finále!', end = '\n')
            return False
        else:
            return True

    def next(self):
        self.history.next_day()
        if(self.qual_is_playing):
            self.qual_is_playing = self.q_next()

            #Kvalifikacia sa skoncila, pripravime si majstrovstva
            if(not self.qual_is_playing):

                final_list = []
                #Z každej kvalifikácie si vypýtame postupujúce tímy
                for q in self.q_list:
                    for l in q.get_winners():
                        final_list.append(l)

                self.world_cup = final.Final(final_list, self.simulator)
        else:
            #Hra sa finale
            if(self.world_cup.has_next()):
                self.world_cup.next()
            else:
                print('Majstrovstvá sa už skončili.', end ='\n')
    def print_tables(self):
        for q in self.q_list:
            q.print_table()
