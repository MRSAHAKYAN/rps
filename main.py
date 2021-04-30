# from winner_definer import *
# from room import *
# from score import ScoreManager
# from player import Player


from room_controller import RoomController
from player import Player
from room import Room
from winner_definer import *

import grpc
import game_pb2
import game_pb2_grpc
import threading
from concurrent import futures

# room_controller = RoomController()

# name = input('Name: ')
# capacity = int(input('Room capacity: '))
# max_score = int(input('Max score: '))
# only_computer = False

# request = {
#     'player': Player(name),
#     'config': {
#         'capacity': capacity,
#         'max_score': max_score,
#         'only_computer': only_computer,
#     },
# }

# #! Словари равны, если они имеют строго одинаковые ключи и строго одинаковые значения для них


# # room_controller.add_player(request)
# print(request['config'])
# print(request['config']['max_score'])
# print(request['config'].get('max_score'))


# # arr = [1, 2, 3, 4, 5]

# # num = int(input())
# # arr.append(num)
# # print(arr)


# rooms = [
#             Room({
#                 'capacity': 4,
#                 'max_score': 5,
#                 'only_computer': False,
#             }),
#             Room({
#                 'capacity': 2,
#                 'max_score': 5,
#                 'only_computer': True,
#             }),
#             Room({
#                 'capacity': 4,
#                 'max_score': 10,
#                 'only_computer': False,
#             }),
#             Room({
#                 'capacity': 4,
#                 'max_score': 5,
#                 'only_computer': True,
#             }),
#             Room({
#                 'capacity': 4,
#                 'max_score': 5,
#                 'only_computer': False,
#             }),
#         ]

# player_config = request['config']


# rooms[0].players = [Player('aaa'), Player('bbb')]
# rooms[4].players = [Player('ddd'), Player('ddd'), Player('ddd')]

# # Room
# result_rooms = [room for room in rooms if room.config == player_config]

# for index, result_room in enumerate(result_rooms):
#     print('index %d: ' % (index + 1))
#     print(result_room.config)
#     print('Заполненность: %d' % len(result_room.players))

# # # max_capacity = [room for room in result_rooms if room.config['capacity'] == max(result_rooms.config['capacity'])]
# # max_capacity = max(result_rooms, key=lambda room: room.config['capacity']) # вместимость

# # [pl1, pl2, pl3]
# # capacity: 4


# fullest_room = max(result_rooms, key=lambda room: len(room.players)) # вместимость

# print('Вы направлены в комнату №%d.' % (rooms.index(fullest_room) + 1))

# print(result_rooms)
# print(max_capacity)
# print(list(map(lambda room: rooms.index(room) + 1, result_rooms)))
# # min - lexicographic order

# # Объект пишется через точку Пример: room.config
# # К словарю обращаемся только так !!! Пример: config['max_score']

# combs = list(Choice)
# print(combs)

# for comb in combs:
#     for i in range(len(combs)):
#         print('%s > %s ? %r' % (comb.name, combs[i].name, comb > combs[i]))
# print('*************')

# for comb in combs:
#     for i in range(len(combs)):
#         print('%s < %s ? %r' % (comb.name, combs[i].name, comb < combs[i]))
# print('*************')
            
# import random
# arr = [1, 2, 3, 4, 5, 6, 7]
# mas = [0] * 20
# print(mas)
# print(random.choice(arr))




def serve():
    room_controller = RoomController()
    thread = threading.Thread(target=room_controller.run)
    thread.start()
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    game_pb2_grpc.add_RoomControllerServicer_to_server(room_controller, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('RoomController started')
    server.wait_for_termination()
    thread.join()

if __name__ == '__main__':
    serve()