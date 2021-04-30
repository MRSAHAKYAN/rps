from score import ScoreManager
from winner_definer import *
from player import Player
from queue import Queue
from exceptions import DuplicateStepException
    
class Room:
    def __init__(self, config, queue):
        self.config = config
        self.players = []
        self.combinations = []
        self.queue = queue
        
    def get_config(self):
        return self.config
    
    def get_capacity(self):
        return self.config['capacity']
    
    def get_players(self):
        return self.players
    
    def is_full(self):
        return len(self.players) == self.config['capacity']
    
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, name):
        for i, player in enumerate(self.players):
            if player.name == name:
                del self.players[i]
                break
        
    def start(self):
        self.score_manager = ScoreManager(self.players)
        
    def do_step(self, name, choice):
        for combination in self.combinations:
           if name == combination['name']:
               print('Duplicate step from player %s' % name)
               # raise поднимает исключение
               raise DuplicateStepException(name) 

        self.combinations.append({
            'name': name,
            'choice': choice,
        })
        # dictionary
        if len(self.combinations) == self.config['capacity']:
            winner_names = WinnerDefiner.get_winners(self.combinations)
            print(winner_names)
            # Отправка информации RoomController'у
            # receivers - получатели
            self.queue.put({
                'receivers': [player.name for player in self.players],
                'winners': winner_names,
            })
            self.combinations = []
            

# room = Room(4, 5)

# room.add_player(Player('Artyom'))
# room.add_player(Player('Igor'))
# room.add_player(Player('Masha'))
# room.add_player(Player('Yulia'))


# room.start()

# print(room.score_manager.score_table)

# # # room.get_combinations([0, 1, 2, 0])
# # # room.get_combinations(0, 1, 2, 0, 5, 2, 6, 2, 6)
# room.get_combinations([
#         {
#             'name': 'Igor',
#             'choice': Choice.ROCK,
#         },
#         {
#             'name': 'Artyom',
#             'choice': Choice.ROCK,
#         },
#         {
#             'name': 'Masha',
#             'choice': Choice.PAPER,
#         },
#         {
#             'name': 'Yulia',
#             'choice': Choice.PAPER,
#         },
# ])

# print(room.score_manager.score_table)
