import logging
import threading
import time

message_format = '%(asctime)s: %(message)s'
logging.basicConfig(format=message_format, level=logging.DEBUG, datefmt='%H:%M:%S')


def test_function(argument):
    logging.info(f'Function{argument} started')
    time.sleep(1)
    logging.info(f'Function{argument} started')


logging.info('process started')
my_task1 = threading.Thread(target=test_function, args=(1, ))
my_task2 = threading.Thread(target=test_function, args=(2, ))
my_tasks = []
my_tasks
#xdist - n- auto - pytestowe uwspółbieżnienie
