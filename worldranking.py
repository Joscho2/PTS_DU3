class WorldRanking(object):

    teams_uefa = []
    teams_world = []

    def __init__(self):
        """Stub verzia WorldRanking systému.
        Vracia zápasy z každej kvalifikácie"""

        #Získanie tímov a ich bodov k 1.1.2015
        #patriace do UEFA
        f = open('rankingUEFA.txt');
        for line in f:
            line = line.strip('\n')
            self.teams_uefa.append(line.split(' '))


        #Tými z ostatných častí sveta ako UEFA
        #pre naplnenie majstrovstiev požadovaným počtom týmov
        #pre testovanie programu
        f = open('rankingWorld.txt');
        for line in f:
            line = line.strip('\n')
            self.teams_world.append(line.split(' '))

    def getTeams(self, s):

        """Vráti zoznam týmov podľa kvalifikácie 's'"""

        if(s == 'uefa'):
            return self.teams_uefa
        elif(s == 'other'):
            return self.teams_world
        else:
            print('Ešte neimplementované!')
            exit()
