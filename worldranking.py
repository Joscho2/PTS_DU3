class WorldRanking(object):

    teams_uefa = []
    teams_world = []

    def __init__(self):
        f = open('rankingUEFA.txt');
        for line in f:
            line = line.strip('\n')
            self.teams_uefa.append(line.split(' '))

        f = open('rankingWorld.txt');
        for line in f:
            line = line.strip('\n')
            self.teams_world.append(line.split(' '))

    def getTeams(self, s):
        if(s == 'uefa'):
            return self.teams_uefa
        elif(s == 'other'):
            return self.teams_world
        else:
            print('Ešte neimplementované!')
            exit()
