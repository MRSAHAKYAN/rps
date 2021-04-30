import redis
import json

# artyom = redis.Redis(host='localhost', port=6379, db=0)
# artyom.set('loh', 'Putin')

# print(artyom.get('loh'))


conn = redis.Redis(host='localhost', port=6379, db=0)

while True:
    # subject = input('Input subject: ')
    command_type = input('Input type of command: ')
    
    name = input('Name: ')
    capacity = int(input('Room capacity: '))
    max_score = int(input('Max score: '))
    only_computer = False

    request = {
        # TODO: player remake to object!
        'name': name,
        'config': {
            'capacity': capacity,
            'max_score': max_score,
            'only_computer': only_computer,
        },
    }

    message = json.dumps({
        'type': command_type,
        'request': request,
    })
    conn.publish('room_controller.command', message)

