class WorldRanking:

    teams = [];

    def __init__(self):
        f = open('rankingUEFA.txt');

        for line in f:
            line = line.strip('\n')
            self.teams.append(line.split(' '))

    def getTeams(self, s):
        if(s == "uefa"):
            return self.teams
        else:
            print("Ešte neimplementované!")
            exit()
