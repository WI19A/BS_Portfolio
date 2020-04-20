from threading import Thread
import time
import random
import queue

class Producer:
    def __init__(self):
        self.product = ['Haselnuss', 'Schnitzelbroetchen', 'Senf']

    def run(self):
        global q
        while True:
            #Random Produktionszeit(0-10 sekunden)
            time.sleep(random.random()*3)
            f = self.product[random.randrange(len(self.product))]
            q.put(f)
            print("Added: {}".format(f))


class Consumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global q
        while True:
            #Random Cosumzeit(0-2 Sekunden)
            time.sleep(random.random()*2)
            print('Queue size: {}'.format(q.qsize()))
            if (not q.empty()):
                f = q.get()
                print("Remove: {}".format(f))
            else:
                print('Consumer is waiting for product!')


if __name__ == '__main__':
    q = queue.Queue(10)
    p = Producer()
    c = Consumer()
    pt = Thread(target=p.run, args = ())
    ct = Thread(target=c.run, args = ())
    pt.start()
    ct.start()




#Methodenaufruf
t=Thread(target=Producer, args=("Producer", ))
t.start()
time.sleep(0.1)
t=Thread(target=Consumer, args=("Consumer", ))
t.start()



