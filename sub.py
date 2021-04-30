import redis
import time

artyom = redis.Redis(host='localhost', port=6379, db=0)
artyom_p = artyom.pubsub()
# subscribe to classical music

# artyom_p.subscribe('music')
artyom_p.psubscribe('music-*')

artyom_p.get_message()

first = True

while True:
    msg = artyom_p.get_message() # => None
    # if msg is not None:
    if msg:
        if first:
            first = not first
            continue
        print(msg)
        print('Я получил сообщение:', msg['data'].decode('utf-8'))
    time.sleep(0.1)

