import threading
import time
import random
import queue

class Prod:
    def __init__(self):
        self.product = ['Haselnuss', 'Schnitzelbroetchen', 'Senf']
        self.next = 0

    def run(self):
        global q
        for i in range(100):
            time.sleep(0.1)
            if (self.next <= i):
                f = self.product[random.randrange(len(self.product))]
                g = self.product[random.randrange(len(self.product))]
                q.put(f)
                q.put(g)
                print("Added: {}".format(f))
                print("Added: {}".format(g))
                self.next += random.random()*10

class Comnsumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global q
        for i in range(100):
            time.sleep(0.1)
            print('Queue size: {}'.format(q.qsize()))
            if (self.next <= i and not q.empty()):
                f = q.get()
                print("Remove: {}".format(f))
                self.next += random.random()*10
            elif q.empty():
                print('Consumer is waiting for product!')

if __name__ == '__main__':
    q = queue.Queue(10)
    p = Prod()
    c = Comnsumer()
    pt = threading.Thread(target=p.run, args = ())
    ct = threading.Thread(target=c.run, args = ())
    pt.start()
    ct.start()