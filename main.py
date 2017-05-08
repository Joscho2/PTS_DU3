import worldranking as wr
import gamesimulator
import gamewrapper
import qualifications.uefaq as uefa
import qualifications.backup_qual as backup
import history

#Spolupráca s WorldRanking systémom,
#ktorý nám dáva tými a ich poradia v svetovej tabuľke
rankingSystem = wr.WorldRanking()

#Vytvorenie histórie, ktorá si bude pamätať výsledky zápaspov,
#posunieme ju ďalším modulom programu
game_history = history.History()

#Simulovanie zápasov, posunieme ho ďalším modulom programu
simulator = gamesimulator.GameSimulator(game_history)

#Vytvorenie zoznamu kvalifikácií na majstrovstvá sveta (Ako napr. UEFA)
qualificationsList =    [uefa.Uefa(simulator, rankingSystem.getTeams('uefa')),
                         backup.Backup(22, rankingSystem.getTeams('other'))]

#Wrapper hry, pre jednoduchšie spracovávanie príkazov a prehľadnosť
#tu, v main.py, spracujeme príkaz od používateľa a vykonanie funkcionality
#neháme na wrapper
wrapper = gamewrapper.GameWrapper(qualificationsList, simulator, game_history)

#Spracovávanie vstupu od používateľa programu
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
