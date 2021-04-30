
# request
# { 'player': player,
#  'config': max_players, max_score, only_computer }

from room import *
from player import Player
import time
import random
import json

import grpc
import game_pb2
import game_pb2_grpc
from winner_definer import Choice

from concurrent import futures
import logging
from queue import Queue

from exceptions import DuplicateStepException


class RoomController(game_pb2_grpc.RoomControllerServicer):
    def __init__(self):
        self.queue = Queue(100)
        self.rooms = [
            Room({
                'capacity': 2,
                'max_score': 5,
                'only_computer': False,
            },
            self.queue),
        ]
        
        self.players_rooms = dict()

    def add_player(self, request):
        #TODO: Попытка найти комнату с такими же параметрами
        def is_suitable_room(room):
            # 1. Если критерии совпадают
            # 2. Комната не заполнена
            return room.config == request['config'] and not room.is_full()
            
        suitable_rooms = list(filter(is_suitable_room, self.rooms))
        suitable_room = random.choice(suitable_rooms)
        new_player = Player(request['name'])
        suitable_room.add_player(new_player)
        self.players_rooms[new_player.name] = suitable_room 
        print(suitable_rooms.index(suitable_room) + 1)
        # self.rooms.append(suitable_room)
        
    def create_room(self, config):
        self.rooms[
            Room(config, self.queue),
        ]
        
        
    def run(self):
        print('Room controller running cycle started')
        while True:
            msg = self.queue.get() 
            if msg:
                print(msg)
                with grpc.insecure_channel('localhost:50052') as channel:
                    stub = game_pb2_grpc.WebServerStub(channel)
                    stub.SendWinners(game_pb2.SendWinnersRequest(
                        receivers=[game_pb2.Player(name=player_name) for player_name in msg['receivers']],
                        winners=[game_pb2.Player(name=player_name) for player_name in msg['winners']],
                    ))
                                
    def RegisterPlayer(self, request, context):
        print('Registering player %s...' % request.player.name)
        print(request)
        # add player
        self.add_player({
            'name': request.player.name,
            'config': {
                'capacity': request.config.capacity,
                'max_score': request.config.max_score,
                'only_computer': request.config.only_computer,
            },
        })
        print('Added player %s  in the room' % request.player.name)
        return game_pb2.RegisterPlayerResponse(status=game_pb2.Status.OK, error_message='Player %s successfully added to the room!' % request.player.name)
                    
    def ChooseCombination(self, request, context):
        player_name = request.player.name
        choice = None
        if request.choice == game_pb2.ChooseCombinationRequest.ROCK:
            choice = Choice.ROCK
        elif request.choice == game_pb2.ChooseCombinationRequest.SCISSORS:
            choice = Choice.SCISSORS
        elif request.choice == game_pb2.ChooseCombinationRequest.PAPER:
            choice = Choice.PAPER
        try:
            self.players_rooms[player_name].do_step(player_name, choice)
        # except обрабатывает исключение
        except DuplicateStepException as e:
            context.abort(grpc.StatusCode.ALREADY_EXISTS, e.message)
            return game_pb2.ChooseCombinationResponse(status=game_pb2.Status.ERROR)
        else:
            return game_pb2.ChooseCombinationResponse(status=game_pb2.Status.OK)
        
    def RemovePlayer(self, request, context):
        player_name = request.player.name
        player_room = self.players_rooms[player_name]
        player_room.remove_player(player_name)
        print('Player %s deleted' % player_name)
        return game_pb2.RemovePlayerResponse()