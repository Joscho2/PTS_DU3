import worldranking as wr
import gamesimulator
import qualifications.uefaq as uefa

rankingSystem = wr.WorldRanking()

simulator = gamesimulator.GameSimulator()
qualificationsList = [uefa.Uefa(gamesimulator, rankingSystem.getTeams("uefa"))]
