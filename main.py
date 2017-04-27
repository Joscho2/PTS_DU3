import worldranking as wr
import gamesimulator
import gamewrapper
import qualifications.uefaq as uefa
import qualifications.backup_qual as backup
import history

rankingSystem = wr.WorldRanking()
game_history = history.History()
simulator = gamesimulator.GameSimulator(game_history)

qualificationsList =    [uefa.Uefa(simulator, rankingSystem.getTeams('uefa')),
                         backup.Backup(22, rankingSystem.getTeams('other'))]

wrapper = gamewrapper.GameWrapper(qualificationsList, simulator, game_history)

while(True):
    com = input()
    if(com == 'next'):
        wrapper.next()
    elif(com == 'quit'):
        break
    elif(com == 'history'):
        game_history.print_history()
    elif(com == 'tables'):
        wrapper.print_tables()
    else:
        print('Neznámy príkaz', end = '\n')
