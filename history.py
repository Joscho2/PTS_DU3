class History(object):
    """Zapamätávanie si výsledkov zápasov"""

    game_stat = []
    day = 0

    def __init__(self):
        super(History, self).__init__()

    def add(self, who, whom, comment):
        self.game_stat.append({	'day' : self.day,
								'who' : who,
								'whom' : whom,
								'comment' : comment})

    def next_day(self):
        self.day += 1

    def print_history(self):
        for s in self.game_stat:
            print	('Deň ' + str(s['day']) + '. ' +
					str(s['comment']) + ' :' + str(s['who']) +
            		'  > porazil > ' +
					str(s['whom']), end='\n')
